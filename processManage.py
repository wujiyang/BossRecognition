#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: wujiyang
@date: 2018-02-02
@brief: manage the process on linux via python os module.
'''

import os 
import psutil
import signal
import sys

from PyQt4 import QtGui
import Tkinter as tk 
from PIL import Image, ImageTk

'''
just open or close some processes as you wish.
'''


def openProcess():
    os.system('gedit')
    # os.system('firefox')
    # os.system('filezilla')


def closeProcess():
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        # print 'pid-%d, pname-%s' %(pid, p.name())
        name = p.name()
        if name == 'firefox' or name == 'chromium-browser':
            os.kill(pid, signal.SIGKILL)
        '''
        chrome only collapses,but not closed, why ???
        '''
    # print len(pids)

def show_image(image_path='vscode.jpg'):
    '''
    show an image in full screen
    '''
    top = tk.Tk()
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(top)
    label.pack()
    label.configure(image = photo )
    top.mainloop()

def main():
    # closeProcess();
    # openProcess();
    show_image();



if __name__ == "__main__":
    main()