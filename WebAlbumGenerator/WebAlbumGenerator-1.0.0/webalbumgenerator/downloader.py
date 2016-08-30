#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import urllib

import tkMessageBox
import tkFileDialog

TRACE = True
DEBUG = False

class Downloader():
	"""ダウンローダ：WebAlbum作成のための、画像ファイル群をダウンロードする。"""

	def __init__(self):
		"""ダウンローダのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__
		return

	def download_images(self):
		"""WebAlbum作成に使う画像をダウンロードする。"""
		if TRACE: print __name__, self.download_images.__doc__
		# 画像の入ったフォルダを選択する。
		is_directory=""
		dirname=tkFileDialog.askdirectory(initialdir=is_directory)
		tkMessageBox.showinfo('WebAlbumGenerator','選択されたフォルダ内の画像で\nWebAlbumページを作成します。')
		
		# 作業ディレクトリを始めに、初期化する。
        # その後、必要な画像ファイル群をすべて作業ディレクトリにコピーする。
		os.system('rm -rf ./images/*')
		os.system('cp -r '+ dirname + '/* ' + './images')
		
		return

