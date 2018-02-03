# /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: wujiyang
@date: 2018-02-02
@brief: manage the process on linux via python os module.
"""

import os
import psutil
import signal
import Tkinter
import platform
from PIL import Image, ImageTk


WINDOWS = 1
LINUX = 2


def init_closelist():
	closelist = []
	with open("CloseList.txt") as f:
		for line in f.readlines():
			closelist.append(line.strip())
	return closelist


def get_system():
	if 'Windows' in platform.system():
		return WINDOWS
	if 'Linux' in platform.system():
		return LINUX


"""
just open or close some processes as you wish.
"""


def open_process():
	os.system('gedit')
	# os.system('firefox')ubantu
	# os.system('filezilla')


def close_process():
	pids = get_pids()
	print pids

	for pid in pids:
		try:
			p = psutil.Process(pid)
			name = p.name()
			if name in init_closelist():
				close_in_diff_system(pid)
		except psutil.NoSuchProcess:
			print("pid not found, may be killed", pid)


def close_in_diff_system(pid):
	now_system = get_system()
	if now_system == WINDOWS:
		os.popen("taskkill.exe /pid:" + str(pid))
	if now_system == LINUX:
		os.kill(pid, signal.SIGKILL)


def get_pids():
	return psutil.pids()


def show_image(image_path='vscode.jpg'):
	"""
	show an image in full screen
	"""
	top = Tkinter.Tk()
	top.title("Yellow Picture!!")
	image = Image.open(image_path)
	photo = ImageTk.PhotoImage(image)
	label = Tkinter.Label(top)
	label.pack()
	label.configure(image=photo)
	top.mainloop()


def main():
	# close_process()
	# open_process()
	show_image()


if __name__ == "__main__":
	main()
