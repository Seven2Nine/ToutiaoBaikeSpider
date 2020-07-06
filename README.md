# ToutiaoBaikeSpider
头条百科-原互动百科 单个词语 异步格式化信息爬取
异步主要针对单个词语对应多个词条的情况，比如李强，王伟这种词

## 使用方式
直接运行 toutiaobaike_spider.py 文件,会在控制台打印该词条信息
> python toutiaobaike_spider.py

## 返回示例
```
[
  {
    "description": "Python（英语发音：/ˈpaɪθən/），是一种面向对象、解释型计算机程序设计语言，由Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。Python是纯粹的自由软件，源代码和解释器CPython遵循 GPL(GNU General Public License)协议。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面 ），然后对其中有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。",
    "icon_path": null,
    "name": "Python",
    "tag": "科学,学科",
    "picture_paths": [
      "//p1-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/d9ad0684ec6a41fa85b99b536e2f3079~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p6-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/586a2f53239c42b28df25f1a65d1b95b~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p6-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/5c031fd1114041f79c28030c418e30ff~tplv-mlhdmxsy5m-q75:0:0.image"
    ],
    "nick_name": "python",
    "source": null,
    "relationship": null,
    "title": null,
    "property_data": {
      "nick_name": "python",
      "外文名": "Python",
      "发明者": "Guido van Rossum",
      "设计者": "Guido van Rossum",
      "创立时间": "1991年",
      "中文名": "蟒蛇",
      "获得荣誉": "2010年度编程语言",
      "最新版本": "3.3.1, 3.2.4, 2.7.5",
      "别名": "蟒蛇语言，胶水语言"
    }
  }
]
```
