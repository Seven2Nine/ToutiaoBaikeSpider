# ToutiaoBaikeSpider
头条百科-原互动百科 单个词语 异步格式化信息爬取
异步主要针对单个词语对应多个词条的情况，比如李强，王伟这种词

## 使用方式

安装依赖  

> pip install requests  
  pip install aiohttp

运行 toutiaobaike_spider.py 文件,会在控制台打印该词条信息  

> python toutiaobaike_spider.py

## 返回示例1
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

## 返回示例2
```
[
  {
    "description": "六小龄童：本名章金莱，汉族，1959年4月12日出生于上海，祖籍浙江绍兴，现为中央电视台、中国电视剧制作中心演员剧团国家一级演员，中国电视艺术家协会演员工作委员会副会长，北京电影家协会青少年电影工作委员会的副会长，2014年10月15日习总书记主持召开的北京文艺座谈会72位代表之一。中宣部“四个一批”人才，无党派人士，荣获国务院特殊津贴。1982年，六小龄童、李世宏和李扬在二十五集神话电视连续剧《西游记》中共同塑造孙悟空一角， 六小龄童被评为中国第六届“金鹰奖”最佳男主角奖及第一届（新时期十年1978年至1987年）“中国电影电视十大明星”奖，同时，以一百二十三万多张选票当选为“中国第二届电视十大明星”第一名。1998年，凭借《西游记续集》中孙悟空一角，获得2000年度由中央电视台颁发的全国十佳优秀演员奖。2004年，在电视剧《欢天喜地七仙女》剧中饰演太上老君。2007年6月，在38集全球首部立体电视连续剧《吴承恩与西游记》中同时扮演吴承恩和孙悟空两个角色。2009年，主演电视剧《北平战与和》，饰演胡适。2013年，主演武侠剧《新燕子李三》饰演李显。2014年9月，在根据《西游记后传》翻拍的《石敢当之雄峙天东》中饰演玉帝。2016年，主演喜剧电影《财迷》。同年，客串出演王宝强电影《大闹天竺》饰演武圣和孙悟空。2017年，执导传记电影《玄奘西游记》。2018年，主演3D魔幻电影《敢问路在何方》，再次饰演孙悟空，并担任艺术总监，该片预计2019年上映。2019年，在韩延执导的魔幻电影《西游记真假美猴王》中以动作捕捉表演的形式再次饰演孙悟空。",
    "icon_path": null,
    "name": "六小龄童",
    "tag": "人物,娱乐人物,艺人",
    "picture_paths": [
      "//p3-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/f6d674e6fa274059a313052a0eb3aaed~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p9-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/d67b281254e1410788f3bc1169b88d47~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p6-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/528718f8fef64913b343f5cf2c72b293~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p9-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/b73e6859e66b4fcc8fc3e48569fad405~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p3-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/acc7ab8001634611aaeeb3bcee06b133~tplv-mlhdmxsy5m-q75:0:0.image",
      "//p6-bk.byteimg.com/tos-cn-i-mlhdmxsy5m/e142539fca8c416f88c51aa4298d952f~tplv-mlhdmxsy5m-q75:0:0.image"
    ],
    "nick_name": null,
    "source": null,
    "relationship": [
      {
        "relationship": "妻子",
        "name": "于虹",
        "baikeid": 19488927
      },
      {
        "relationship": "女儿",
        "name": "章同童",
        "baikeid": 19777212
      },
      {
        "relationship": "父亲",
        "name": "章宗义",
        "baikeid": 2837254
      },
      {
        "relationship": "好友",
        "name": "马德华",
        "baikeid": 10280285
      },
      {
        "relationship": "好友",
        "name": "迟重瑞",
        "baikeid": 312820
      },
      {
        "relationship": "好友",
        "name": "闫怀礼",
        "baikeid": 312822
      }
    ],
    "title": null,
    "property_data": {
      "中文名": "章金莱",
      "别名": "六小龄童（艺名）",
      "国籍": "中国",
      "职业": "国家一级演员",
      "代表作品": "《",
      "主要成就": null,
      "性别": "男",
      "出生地": "上海市",
      "出生日期": "1959年4月12日",
      "民族": "汉族",
      "毕业院校": "浙江省昆剧团艺校",
      "身高": "172cm",
      "体重": "68kg",
      "血型": "O型",
      "爱好": " ",
      "职务": "中国人民大学荣誉教授",
      "祖籍": "浙江省绍兴市上虞区道墟镇",
      "工作单位": "中国电视剧制作中心演员剧团",
      "单位地址": "北京市宣武区广外大街2号",
      "父亲": "章宗义（六龄童）",
      "配音搭档": "李世宏、李扬"
    }
  }
]
```
