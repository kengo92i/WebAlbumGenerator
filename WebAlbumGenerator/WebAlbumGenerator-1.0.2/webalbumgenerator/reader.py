#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

TRACE = True
DEBUG = False

class Reader(object):
	"""リーダ：WebAlbumページを作成するために必要な情報を読み込む。"""

	def __init__(self):
		"""リーダのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__
		return


	def photo_count(self, path):
		"""指定したフォルダの画像ファイル数を数える。"""
		if TRACE: print __name__, self.photo_count.__doc__
		
		if not os.path.isdir(path): return 0
		i=0
		for root, dirs, files in os.walk(path):
			i+=len(files)
		return i
