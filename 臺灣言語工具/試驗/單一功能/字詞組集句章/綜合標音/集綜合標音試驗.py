# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import unittest
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.基本元素.字 import 字
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.字詞組集句章.綜合標音.集綜合標音 import 集綜合標音
from 臺灣言語工具.字詞組集句章.綜合標音.詞組綜合標音 import 詞組綜合標音
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 無音

class 集綜合標音試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.粗胚 = 文章粗胚()
	def tearDown(self):
		pass
	def test_基本試驗(self):
		媠某 = self.分析器.產生對齊組('美女', 'sui2-boo2')
		美女 = self.分析器.產生對齊組('美女', 'mi2-lu2')
		集物件 = 集([媠某, 美女])
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(len(標音集.綜合詞組), 2)
		self.assertEqual(標音集.綜合詞組[0], 詞組綜合標音(閩南語字綜合標音, 媠某))
		self.assertEqual(標音集.綜合詞組[1], 詞組綜合標音(閩南語字綜合標音, 美女))
	def test_有無音字(self):
		集物件 = 集([self.分析器.產生對齊組('點仔膠', 'tiam2-a2-ka1'),
				self.分析器.建立組物件('，'),
				self.分析器.產生對齊組('黏著跤', 'liam5-tioh8 kha1'),
				self.分析器.建立組物件('，'),
				])
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(len(標音集.綜合詞組), 4)
		self.assertEqual(len(標音集.綜合詞組[0].綜合字), 3)
		self.assertEqual(len(標音集.綜合詞組[1].綜合字), 1)
		self.assertEqual(len(標音集.綜合詞組[2].綜合字), 3)
		self.assertEqual(len(標音集.綜合詞組[3].綜合字), 1)
		self.assertEqual(標音集.綜合詞組[0].綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音集.綜合詞組[0].綜合字[1], 閩南語字綜合標音(字('仔', 'a2')))
		self.assertEqual(標音集.綜合詞組[0].綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音集.綜合詞組[1].綜合字[0], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音集.綜合詞組[2].綜合字[0], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音集.綜合詞組[2].綜合字[1], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音集.綜合詞組[2].綜合字[2], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音集.綜合詞組[3].綜合字[0], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音集.綜合詞組[0].連字音, 'tiam2-a2-ka1')
		self.assertEqual(標音集.綜合詞組[1].連字音, '')
		self.assertEqual(標音集.綜合詞組[2].連字音, 'liam5-tioh8 kha1')
		self.assertEqual(標音集.綜合詞組[3].連字音, '')

	def test_孤字轉json格式(self):
		白組物件 = self.分析器.產生對齊組('一', 'tsit8')
		文組物件 = self.分析器.產生對齊組('一', 'it4')
		集物件 = 集([白組物件, 文組物件])
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(標音集.轉json格式(), [
			{"詞組綜合標音":[{"型體":"一", "臺羅數字調":"tsit8", "臺羅閏號調":"tsi̍t", "通用數字調":"zit6", "吳守禮方音":"⿳⿳⿳ㄐㄧ㆐ㆵ"}],
			"連字音":"tsit8"},
			{"詞組綜合標音":[{"型體":"一", "臺羅數字調":"it4", "臺羅閏號調":"it", "通用數字調":"it7", "吳守禮方音":"⿳ㄧㆵ"}],
			"連字音":"it4"}
			])
		組的標音詞組 = [詞組綜合標音(閩南語字綜合標音, 白組物件).轉json格式()]
		組的標音詞組.append(詞組綜合標音(閩南語字綜合標音, 文組物件).轉json格式())
		self.assertEqual(標音集.轉json格式(), 組的標音詞組)

	def test_一詞轉json格式(self):
		集物件 = self.分析器.產生對齊集('椅仔', 'i2-a2')
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(標音集.轉json格式(), [
			{"詞組綜合標音":[
			{"型體":"椅", "臺羅數字調":"i2", "臺羅閏號調":"í", "通用數字調":"i4", "吳守禮方音":"⿳ㄧˋ"},
			{"型體":"仔", "臺羅數字調":"a2", "臺羅閏號調":"á", "通用數字調":"a4", "吳守禮方音":"⿳ㄚˋ"}
			], "連字音":"i2-a2"}
			])

	def test_文白一詞轉json格式(self):
		白組物件 = self.分析器.產生對齊組('大人', 'tua7-lang5')
		文組物件 = self.分析器.產生對齊組('大人', 'tai7-jin5')
		集物件 = 集([白組物件, 文組物件])
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(標音集.轉json格式(), [
			{"詞組綜合標音":[
				{"型體":"大", "臺羅數字調":"tua7", "臺羅閏號調":"tuā", "通用數字調":"dua2", "吳守禮方音":"⿳⿳⿳ㄉㄨㄚ˫"},
				{"型體":"人", "臺羅數字調":"lang5", "臺羅閏號調":"lâng", "通用數字調":"lang5", "吳守禮方音":"⿳⿳ㄌㄤˊ"}],
				"連字音":"tua7-lang5"},
			{"詞組綜合標音":[
				{"型體":"大", "臺羅數字調":"tai7", "臺羅閏號調":"tāi", "通用數字調":"dai2", "吳守禮方音":"⿳⿳ㄉㄞ˫"},
				{"型體":"人", "臺羅數字調":"jin5", "臺羅閏號調":"jîn", "通用數字調":"rin5", "吳守禮方音":"⿳⿳⿳ㆢㄧㄣˊ"}],
				"連字音":"tai7-jin5"},
			])
		組的標音詞組 = [詞組綜合標音(閩南語字綜合標音, 白組物件).轉json格式()]
		組的標音詞組.append(詞組綜合標音(閩南語字綜合標音, 文組物件).轉json格式())
		self.assertEqual(標音集.轉json格式(), 組的標音詞組)

if __name__ == '__main__':
	unittest.main()
