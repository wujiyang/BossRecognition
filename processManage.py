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


def main():
    closeProcess();
    openProcess();



if __name__ == "__main__":
    main()