import hashlib
import re, requests, random

"""
自动检测	auto	"中文":"zh"	  ,      "英语":"en",
"粤语":	"yue"	  ,      "文言文": "wyw"	,    "日语"	:"jp",
"韩语":	"kor"	 ,       "法语"	:"fra"	 ,   "西班牙语":	"spa",
"泰语":	"th"	 ,       "阿拉伯语": "ara"	 ,   "俄语"	:"ru",
"葡萄牙语" :"pt"	  ,  "德语":	"de"	    "意大利语"	:"it",
"希腊语" :  "el"	  ,  "荷兰语" :"nl"	 ,   "波兰语" :"pl",
"""

# APP ID：20210401000757212

# 密钥：4dyBrna0w29WZNk2RoGd

language_dict = {
    1: "中文", 2: "英语", 3: "粤语", 4: "文言文", 5: "日语",
    6: "韩语", 7: "法语", 8: "泰语", 9: "西班牙语", 10: "阿拉伯语", 11: "俄语", 17: "波兰语"
}


def LanguafeCode(key):
    Code = {
        "中文": "zh", "英语": "en",
        "粤语": "yue", "文言文": "wyw", "日语": "jp",
        "韩语": "kor", "法语": "fra", "西班牙语": "spa",
        "泰语": "th", "阿拉伯语": "ara", "俄语": "ru",
        "葡萄牙语": "pt", "德语": "de",
        "意大利语": "it", "希腊语": "el", "荷兰语": "nl", "波兰语": "pl",
    }
    return Code.get(key,None)


def translate(q,lan_to,lan_from="auto"):
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    appid = 20210401000757212
    appkey = "4dyBrna0w29WZNk2RoGd"
    salt = random.randint(1, 65536)
    sign = hashlib.md5((str(appid) + str(q) + str(salt) + str(appkey)).encode('utf-8')).hexdigest()
    params = {
        'q': q,
        'from': lan_from,
        'to': lan_to,
        'appid': appid,
        'salt': salt,
        'sign': sign,
    }

    r = requests.get(url, params=params)
    txt = r.json()
    if txt.get('trans_result', -1) == -1:
        print('ERROR Code：{}'.format(txt))
        return q
    return txt['trans_result'][0]



if __name__ == '__main__':
    print("翻译语言所对应代码：")
    for key,val in language_dict.items():
        print("{0}:{1}".format(str(key),val))
    choice = int(input("请选择需要翻译的语言："))
    Code = LanguafeCode(language_dict.get(choice,None))
    context = input("你需要翻译的内容：")
    txt = translate(context, Code)
    print("{0} 的 {1} 翻译成 {2} ".format(context,language_dict.get(choice,None),txt.get("dst",None)))
