#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: wujiyang
@date: 2018-02-01
@brief: Add caffe to PYTHONPATH
'''

import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

caffe_path = '/home/wujiyang/caffe'

# Add caffe to PYTHONPATH
caffe_path = osp.join(caffe_path, 'python')
add_path(caffe_path)
