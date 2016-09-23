#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys

TRACE = True
DEBUG = False

class Writer(object):
	"""ライタ：変換した画像ファイルを使ってWebAlbumページとして書き出す。"""

	def __init__(self, base_directory, year, month, day, title, filename ,number_of_images):
		"""ライタのコンストラクタ。Albumページに必要な情報を受け取る。"""
		if TRACE: print __name__, self.__init__.__doc__
		self._base_directory = base_directory
		self._year = year
		self._month = month
		self._day = day
		self._title = title
		self._filename = filename
		self._number_of_images = number_of_images
		return

	def write(self):
		"""WebAlbumページを、指定したファイルに書き出す。"""
		if TRACE: print __name__, self.write.__doc__
		filename_string = self._year + self._month + self._day + "_" + self._filename
		html_filename = os.path.join(self._base_directory, filename_string+'.html')
		with open(html_filename, 'wb') as a_file:
			self.write_header(a_file)
			self.write_body(a_file)
			self.write_footer(a_file)
		return

	def write_body(self, file):
		"""ボディを書き出す。つまり、画像を表示するページの骨組みを作る。"""
		if TRACE: print __name__, self.write_body.__doc__
		file.write("<body>\n<center>\n")
		file.write("<font size=\"6\">"+self._year+"年"+self._month+"月"+self._day+"日 "+self._title+"</font><br>\n</center>\n<div id=\"wrap\">\n")

		for nth in xrange(1, self._number_of_images+1):
			self.write_img(file, nth)
		
		return

	def write_img(self, file, number):
		"""画像を表示するタグを書き出す。"""
		if DEBUG: print __name__, self.write_img.__doc__
		number_string = ("000" + str(number))[-3:]
		images_string = self._year+self._month+"_"+self._day+"_"+self._filename
		file.write("\t<a href=\" "+images_string+"/output_b/photo"+number_string+".JPG\" rel=\"lightbox[CategoryA]\"><img class=\"smallimage\" src=\" "+images_string+"/output_s/photo"+number_string+".JPG\"  alt=\"タイトル #1\" /></a>\n")

	def write_footer(self, file):
		"""フッタを書き出す。"""
		if TRACE: print __name__, self.write_footer.__doc__
		name_string = "WebAlbumGenerator written by Python"
		date_string = datetime.date.today().strftime("%Y/%m/%d")
		time_string = datetime.datetime.now().strftime("%H:%M:%S")
		file.write("<hr>\nCreated using " + name_string + " " + date_string + " " + time_string + "</div>\n</body>\n</html>\n")
		return
	
	def write_header(self, file):
		"""ヘッダを書き出す。"""
		if TRACE: print __name__, self.write_header.__doc__
		file.write("<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"ja\">\n<head>\n <title>"+self._title+"</title>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\n<link href=\"css/style.css\" rel=\"stylesheet\" type=\"text/css\" />\n<link href=\"css/lightbox.css\" rel=\"stylesheet\" type=\"text/css\" media=\"screen\" />\n<script type=\"text/javascript\" src=\"js/script.js\"></script>\n<script type=\"text/javascript\" src=\"js/prototype.js\"></script>\n<script type=\"text/javascript\" src=\"js/scriptaculous.js?load=effects,builder\"></script>\n<script type=\"text/javascript\" src=\"js/lightbox.js\"></script>\n</head>\n")
		return
