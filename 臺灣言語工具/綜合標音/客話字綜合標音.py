# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音


class 客話字綜合標音:
    型體 = None
    臺灣客話 = None

    def __init__(self, 字物件, 音標一定愛著=False):
        if not isinstance(字物件, 字):
            raise 型態錯誤('傳入來的毋是字物件！{0}，{1}'.format(type(字物件), str(字物件)))
        self.型體 = 字物件.型
        if 字物件.音 == 無音:
            self.臺灣客話 = 無音
        elif 字物件.音 in 標點符號:
            self.臺灣客話 = 字物件.音
        else:
            客音 = 臺灣客家話拼音(字物件.音)
            self.臺灣客話 = 客音.音標
            if 音標一定愛著 and not self.標音完整無():
                raise 解析錯誤('音標無合法：{0}，{1}，{2}'.
                           format(字物件, self.型體, self.臺灣客話))

    def 轉json格式(self):
        return {"型體": self.型體, "臺灣客話": self.臺灣客話}

    def 標音完整無(self):
        return (self.型體 is not None and self.臺灣客話 is not None)

    def __repr__(self):
        return self.轉json格式()

    def __str__(self):
        return self.轉json格式()

    def __eq__(self, 別个):
        return isinstance(別个, 客話字綜合標音) and self.型體 == 別个.型體 and \
            self.臺灣客話 == 別个.臺灣客話
