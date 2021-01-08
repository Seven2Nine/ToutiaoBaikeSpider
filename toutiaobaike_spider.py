# -*- coding: utf-8 -*-
import json
import time
import aiohttp
import asyncio
import requests

from urllib import parse


class ToutiaoSpider:
    def __init__(self, term_name):
        self._timeout = aiohttp.ClientTimeout(total=30)
        self._headers = {
            "Referer": "https://www.baike.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.132 Safari/537.36",
        }
        self._term_name = term_name
        self._base_url = f"https://www.baike.com/wiki/{term_name}"
        self._datalist = []
        self._final_datalist = []

    async def __get_html(self, url):
        """协程方式的获取页面"""
        sem = asyncio.Semaphore(20)  # 信号量，控制协程数
        async with sem:
            async with aiohttp.ClientSession(headers=self._headers, timeout=self._timeout) as session:
                async with session.get(url) as resp:
                    # print(resp.status)
                    content = resp.text()
                    real_url = resp.url
                    return await content, real_url

    def __get_html_single(self, url):
        """普通方式的获取页面"""
        response = requests.get(url, timeout=30, headers=self._headers)
        return response.text, response.url

    async def __get_content(self, url):
        """
        获取页面反回内容
        :param url: 页面url
        :return:
        """
        term_content, term_url = await self.__get_html(url)
        term_main_data = term_content.split("data: ")[1].split("}</script>")[0]
        # print(term_main_data)
        term_main_data = json.loads(term_main_data)
        term_main_data = term_main_data[0] if isinstance(term_main_data, list) and len(term_main_data) > 0 else {}
        try:
            term_main_data["WikiDoc"]['Abstract'] = json.loads(term_main_data.get('WikiDoc').get('Abstract'))
            term_main_data["WikiDoc"]["Content"] = json.loads(term_main_data.get('WikiDoc').get("Content"))
            term_main_data["WikiDoc"]['InfoBox'] = term_main_data.get('WikiDoc').get('InfoBox')
            term_main_data["WikiDoc"]["UGCModule"] = term_main_data.get('WikiDoc').get("UGCModule")
        except Exception as e:
            term_main_data["WikiDoc"]['Abstract'] = {}
            term_main_data["WikiDoc"]['UGCModule'] = {}
            term_main_data["WikiDoc"]["Content"] = []
            term_main_data["WikiDoc"]["InfoBox"] = []
        self._datalist.append({
            "term": self._term_name,
            "url": term_url.__str__(),
            "content": term_main_data
        })

    async def __get_pic(self, url):
        """协程方式的获取圖片"""
        sem = asyncio.Semaphore(20)  # 信号量，控制协程数
        async with sem:
            async with aiohttp.ClientSession(headers=self._headers) as session:
                async with session.get(url) as resp:
                    content = resp.read()
                    return await content

    def __start_spider(self, term):
        terms_list = []
        base_url = f"https://www.baike.com/wiki/{term}"
        content, real_url = self.__get_html_single(base_url)
        main_datas = json.loads(content.split("data: ")[1].split("}</script>")[0])
        for main_data in main_datas:
            terms_list = main_data.get("WikiDoc").get('PolysemyList')
        if terms_list is None:
            terms_list = []
            terms_list.append({"WikiDocID": ""})
        return terms_list

    @staticmethod
    def __get_assign_obj(datas, key, value):
        """
        根据key-value获取列表的指定对象
        :return:
        """
        for data in datas:
            if data.get(key) == value:
                return data
            else:
                continue
        return dict()

    def __get_all_text(self, data, text):
        """
        获取所有文本
        :return:
        """
        for k, v in data.items():
            if k == "text" or k == "OriText":
                text += v
            if isinstance(v, dict):
                text = self.__get_all_text(v, text)
            if isinstance(v, list):
                for i, value in enumerate(v):
                    if isinstance(value, dict):
                        text = self.__get_all_text(value, text)
                    if isinstance(value, list):
                        for j, value2 in enumerate(value):
                            if isinstance(value2, dict):
                                text = self.__get_all_text(value2, text)
        return text

    def __get_attr(self, item_data):
        item_data.pop("URL")
        item_data.pop("tag")
        item_data.pop("name")
        item_data.pop("title")
        item_data.pop("baike_id")
        item_data.pop("description")
        item_data.pop("picture_paths")
        try:
            item_data.pop("relationship")
        except:
            pass
        return item_data

    def get_all_data(self, size):
        i = 0
        tasks = []
        terms_list = self.__start_spider(self._term_name)
        if not terms_list:
            # 词条不存在
            return False
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()  # 获取事件循环
        for i, term_data in zip(range(size), terms_list):
            tasks.append(self.__get_content(self._base_url + f"/{term_data.get('WikiDocID')}"))
            # term_content, term_url = await self.__get_html(self._base_url + f"/{term_data.get('doc_id')}")

        loop.run_until_complete(asyncio.wait(tasks))  # 激活协程
        loop.close()
        return self._datalist

    def data_handle4save(self, datalist):
        """
        获取真正需要的数据并转换为保存需要的格式
        :param datalist:
        :return:
        """
        new_datalist = []
        for data in datalist:
            content = data.get("content").get("WikiDoc")
            imglist = json.loads(content.get('UGCModule', {}).get("image", {}).get("Data", "{}")).get('image_list')
            relationship = content.get('ModuleList', [])[0].get("Data", {}) if content.get('ModuleList', []) else {}
            new_data = {
                "name": content.get("Title"),
                "URL": parse.unquote(data.get("url")),
                "baike_id": content.get("WikiDocID"),
                "title": content.get('Subtitle') if content.get('Subtitle') != content.get("Title") else None,
                "description": self.__get_all_text(
                    {"summary": content.get('Abstract')}, ""),
                "tag": ",".join(content.get('CategoryList')[0] if content.get('CategoryList') else []),
                "picture_paths": [picture_url.get("uri") for picture_url in (imglist if imglist else [])]
            }
            # 判断有无别名,有的话添加
            if new_data.get("name") != data.get("term"):
                new_data.update({"nick_name": data.get("term")})

            # 添加属性
            for attribute in content.get("InfoBox"):
                try:
                    new_data.update({attribute.get("Name"): self.__get_all_text(attribute, "")})
                except Exception:
                    try:
                        new_data.update({attribute.get("Name"): attribute.get("Value")[0].get("Value")})
                    except Exception as e:
                        print(f"词条{data.get('term')}的属性->{attribute}  不规范\n 错误信息：{e}")
            # 添加人物关系
            try:
                relationships = json.loads(relationship)
                # relationships = json.loads(relationship)
                new_relationship = []
                for relationship in relationships:
                    new_relationship.append({
                        "main": data.get("term"),
                        "type": relationship.get("relationship"),
                        "name": relationship.get("title"),
                        "baikeid": relationship.get("wiki_doc_id")
                    })
                new_data.update({"relationship": new_relationship})
            except Exception:
                pass
                # print("该词条无人物关系")
            new_datalist.append(new_data)

        return new_datalist

    def data_handle4show(self, datalist):
        """
        处理数据为展示用的格式
        :param datalist:
        :return:
        """
        new_datalist = []
        for data in datalist:
            new_data = {
                "description": data.get("description"),
                "icon_path": data.get("picture_path")[0] if data.get("picture_path") else None,
                "name": data.get("name"),
                "tag": data.get("tag"),
                "picture_paths": data.get("picture_paths"),
                "nick_name": data.get("nick_name"),
                "source": data.get("url"),
                "relationship": data.get("relationship"),
                "title": data.get("title"),
                "property_data": self.__get_attr(data),
            }
            new_datalist.append(new_data)
        return new_datalist


if __name__ == '__main__':
    start_time = time.time()
    toutiao = ToutiaoSpider("python")  # 初始化类，传入要爬取信息的词条
    data_list = toutiao.get_all_data(50)  # 获取爬取列表（词条存在同名情况） 参数为要获取的数量
    if not data_list:
        print("词条不存在")
    else:
        new_data_list = toutiao.data_handle4show(toutiao.data_handle4save(data_list))
        print(json.dumps(new_data_list, ensure_ascii=False, indent=2))
