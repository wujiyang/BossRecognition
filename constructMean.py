#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
@Author: wujiyang
@Time: 2017/11/24 15:30:24
@Brief: construct mean file for caffe data layer
'''

## convert mean.binaryproto to mean.npy
# import caffe
# import numpy as np

# MEAN_PROTO_PATH = 'mean.binaryproto'               # source path
# MEAN_NPY_PATH = 'mean.npy'                         # save path

# blob = caffe.proto.caffe_pb2.BlobProto()           # create protobuf blob
# data = open(MEAN_PROTO_PATH, 'rb' ).read()         # read mean.binaryproto
# blob.ParseFromString(data)                         # parsing the data to caffe blob

# array = np.array(caffe.io.blobproto_to_array(blob))# 将blob中的均值转换成numpy格式，array的shape （mean_number，channel, hight, width）
# mean_npy = array[0]                                # 一个array中可以有多组均值存在，故需要通过下标选择其中一组均值
# np.save(MEAN_NPY_PATH ,mean_npy)


## construct mean.npy according to mean value
import numpy as np

MEAN_NPY_PATH = 'mean.npy'

mean = np.ones([3,256, 256], dtype=np.float)
mean[0,:,:] = 127.5
mean[1,:,:] = 127.5
mean[2,:,:] = 127.5

np.save(MEAN_NPY_PATH, mean)


## load mean.npy
# import numpy as np

# mean_npy = np.load(MEAN_NPY_PATH)
# mean = mean_npy.mean(1).mean(1)