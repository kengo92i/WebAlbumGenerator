#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import locale
import shutil
import sys

import Tkinter
import tkFileDialog
import tkMessageBox

import downloader
import translator
import writer
import reader

from Tkinter import *

TRACE = True
DEBUG = False

class Example(Tkinter.Tk):
	"""WebAlbumGeneratorを開く"""

	def __init__(self):
		"""WebAlbumGeneratorのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__
		Tkinter.Tk.__init__(self)
		self.my_widgets()
		
	def my_widgets(self):
		"""ウィジェットを設定する"""

		#rootの設定
		self.title('WebAlbumGenerator v0.1')
		self.geometry('400x520+180+40')
		self.minsize(400, 520)
		self.maxsize(400, 520)
		
		#見出し
		self._label = Label(self, text = 'WebAlbum自動生成システム')
		self._label.pack(padx = 5, pady = 5, fill=BOTH)
		self._label.pack()
		
		#題名の設定
		self._title_frame = LabelFrame(self, text = '題名')
		self._title_frame.pack(padx = 5, pady = 5, fill=BOTH)

		self._title = Text(self._title_frame, height=1)
		self._title.insert(END, 'ほげほげページ')
		
		self._title.pack(fill = BOTH, expand = True)
		self._title_frame.pack()
		
		#ファイル名の設定
		self._filename_frame = LabelFrame(self, text = 'ファイル名')
		self._filename_frame.pack(padx = 5, pady = 5, fill=BOTH)
		
		self._filename = Text(self._filename_frame, height=1)
		self._filename.insert(END, 'WebAlbumSample')
		
		self._filename.pack(fill = BOTH, expand = True)
		self._filename_frame.pack()
		
		#年度の設定
		self._year_frame = LabelFrame(self, text = '年度')
		self._year_frame.pack(padx = 5, pady = 5, fill=BOTH)
		
		self._year = Text(self._year_frame, height=1)
		self._year.insert(END, '2014')
		
		self._year.pack(fill = BOTH, expand = True)
		self._year_frame.pack()
		
		self._frame = Frame(self)
		self._frame.pack()
		
		#月の設定
		self._month_frame = LabelFrame(self._frame, text = '月')
		self._month_frame.pack(padx = 5, pady = 5, fill=BOTH, side=LEFT)
		
		self._month = Text(self._month_frame, height=1, width=25)
		self._month.insert(END, '4')
		
		self._month.pack(fill = BOTH, expand = True)
		self._month_frame.pack()
		
		
		#日の設定
		self._day_frame = LabelFrame(self._frame, text = '日')
		self._day_frame.pack(padx = 5, pady = 5, fill=BOTH)
		
		self._day = Text(self._day_frame, height=1, width=25)
		self._day.insert(END, '5')
		
		self._day.pack(fill = BOTH, expand = True)
		self._day_frame.pack()
		
		
		#説明表示
		self._info_frame = LabelFrame(self, text = '説明')
		self._info_frame.pack(padx = 5, pady = 5, fill=BOTH)
		
		self._info = Text(self._info_frame, height=11)
		self._info.insert(END, 'これはWebAlbum自動生成プログラムです。\n\n')
		self._info.insert(END, '1. 始めにWebAlbumに載せる画像をまとめたフォルダを作る。\n')
		self._info.insert(END, '2. 上記の入力事項を変更する。\n')
		self._info.insert(END, '3. その後、[作成]をクリックする。\n')
		self._info.insert(END, '4. WebAlbumを作りたい画像が入ったフォルダを選択する。\n')
		self._info.insert(END, '5. HTMLページが自動生成されるので、プラウザで確認する。\n')
		self._info.insert(END, '6. 作成したWebAlbumページを公開する。\n\n')
		self._info.insert(END, '--- 今江健悟')
		
		self._info.config(state=DISABLED)
		self._info.pack(fill = BOTH, expand = True)
		
		#ボタンの設定
		button_frame = LabelFrame(self, text = '操作')
		button_frame.pack(padx = 5, pady = 5, side = RIGHT)
		
		button_list = Frame(button_frame)
		Button(button_list, text = '作成', command = lambda : self.generator()).pack(side=LEFT)
		Button(button_list, text = '終了', command=lambda : quit(self)).pack(side=LEFT)
		button_list.pack()
		
		return

	def generator(self):
		"""WebAlbumを作成する。"""
		if TRACE: print __name__, self.generator.__doc__
		
		# ホームディレクトリの直下のデスクトップのディレクトリに、
		# WebAlbumというディレクトリを作成する。
		# すでに存在すれば、当該ディレクトリを消して、新たに作り、
		# 存在しなければ、当該ディレクトリを作成する。
		home_directory = os.environ['HOME']
		base_directory = home_directory + '/Desktop/WebAlbum/'
		if os.path.isdir(base_directory):
			shutil.rmtree(base_directory)
		os.makedirs(base_directory)
        
		
		# 必要な情報をGUIから受け取る。
		adjust = lambda value : ("00" + str(value))[-2:]
		year = self._year.get('1.0', END).rstrip().encode('utf_8')
		month = adjust( self._month.get('1.0', END).rstrip().encode('utf_8') )
		day = adjust( self._day.get('1.0', END).rstrip().encode('utf_8') )
		title = self._title.get('1.0', END).rstrip().encode('utf_8')
		filename = self._filename.get('1.0', END).rstrip().encode('utf_8')

		
		# WebAlbumに必要な画像ファイルをダウンロードする。
		a_downloader = downloader.Downloader()
		a_downloader.download_images()
		
		
		# 与えられた画像をAlbumページ用にリサイズ、リネイムする。
		a_translator = translator.Translator(year, month, day, filename)
		a_translator.rename_and_resize()
		
		
		# 出力結果から、総画像数を読み取る。
		a_reader = reader.Reader()
		number_of_images = a_reader.photo_count('./images')
		
		
		# ライターに出力となる情報を渡して、Webページを作成してもらう。
		a_writer = writer.Writer(base_directory, year, month, day, title, filename, number_of_images)
		a_writer.write()
		
		
		# 作業の終了を表示、WebAlbumページをブラウザで開く。
		print "変換が終了し、htmlファイルを出力しました。"
		html_filename = year + month + day + "_" + filename + '.html'
		os.system('open ~/Desktop/WebAlbum/'+html_filename)
		os.system('rm -rf ~/Desktop/PictureAutosize')
		os.system('rm -rf ./images/*')
		quit(self)
		return 0


	def open(self):
		"""WebAlbumGeneratorを開く"""
		if TRACE: print __name__, self.open.__doc__

		self.mainloop()

		return


	def main(self):
		"""プログラム起動"""
		if TRACE: print __name__, self.main.__doc__

		self.open()

		return

if __name__ == '__main__':
	e = Example()
	e.main()