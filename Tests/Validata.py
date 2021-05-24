import re


class ValiData:
    value = ""

    def __init__(self, value):
        self.value = value

    """判断是否为空"""

    def Is_Null(self):
        if len(self.value) == 0:
            return 0
        return 1

    """检查手机号码是否匹配"""

    def Is_Phone(self):
        if self.Is_Null():
            string = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
            if string.search(self.value) == None:
                return 0
            return 1
        return 0


if __name__ == "__main__":
    phone = input("请输入号码")
    x = ValiData(phone)
    print(x.value, x.Is_Phone())
