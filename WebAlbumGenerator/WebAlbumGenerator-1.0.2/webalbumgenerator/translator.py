#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

import reader

TRACE = True
DEBUG = False

class Translator(object):
	"""トランスレータ：画像ファイル群をWebALbum用に変換する。"""

	def __init__(self, year, month, day, filename):
		"""トランスレータのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__
		self._year = year
		self._month = month
		self._day = day
		self._filename = filename
		self._home_directory = os.environ['HOME']
		self._base_directory = self._home_directory + '/Desktop/WebAlbum/'
		self._output_b = self._home_directory+'/Desktop/PictureAutosize/01.size_rename/output_b'
		self._output_s = self._home_directory+'/Desktop/PictureAutosize/01.size_rename/output_s'
		return

	def rename_and_resize(self):
		"""画像ファイル群をリネーム・リサイズし、出力する。"""
		if TRACE: print __name__, self.rename_and_resize.__doc__
		os.system('sh PictureAutosize/01.size_rename/renameAndResize.sh')
		images_dir = self._base_directory +'/'+self._year+self._month+'_'+self._day+'_'+self._filename
		if os.path.isdir(images_dir):
			shutil.rmtree(images_dir)
		os.makedirs(images_dir)
		os.system('cp -r '+ self._output_b + ' ' + images_dir)
		os.system('cp -r '+ self._output_s + ' ' + images_dir)
		os.system('cp -r '+ './asset/*' + ' ' + self._base_directory)

