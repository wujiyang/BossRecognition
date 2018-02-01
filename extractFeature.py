#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: wujiyang
@date: 2018-02-01
@brief: extract face image feature with caffe model
'''

import cv2
import math
import sklearn
import numpy as np
import skimage
import _init_paths
import caffe

import sklearn.metrics.pairwise as pw

def readImageList(listFile):
    imageList = []
    file = open(listFile)
    lines = file.readlines()
    file.close()
    for line in lines:
        image = line.strip('\n')
        imageList.append(image)

    return imageList


def initFeatureExtractor():
    print 'feature extraction model initilizing...'
    deployPrototxt = "./caffemodel/sphereface_deploy_36.prototxt"
    modelFile = "./caffemodel/sphereface_model_36.caffemodel"
    caffe.set_mode_gpu()
    caffe.set_device(0)
    net = caffe.Net(deployPrototxt, modelFile,caffe.TEST)
    return net

def setTransformer(net):
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape}) 
    transformer.set_transpose('data', (2,0,1))                        # move image channels to outermost dimension
    transformer.set_mean('data', np.load('mean.npy').mean(1).mean(1)) # subtract the dataset-mean value in each channel
    # cv.imread: BGR in [0, 255] do not need the next two step
    # transformer.set_raw_scale('data', 255)                            # rescale from [0, 1] to [0, 255]
    # transformer.set_channel_swap('data', (2,1,0))                     # swap channels from RGB to BGR

    return transformer


def extractFeature(net, transformer, img): 
    net.blobs['data'].reshape(1, 3, 112, 96) 
    transformed_image = transformer.preprocess('data', img)
    net.blobs['data'].data[...] = transformed_image

    ### perform net forward
    output = net.forward()
    feature = np.float64(output['fc5'])

    return feature


def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(a,b):
        part_up += a1*b1
        a_sq += a1**2
        b_sq += b1**2
    part_down = math.sqrt(a_sq*b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down


def main():
    '''
    test function
    '''
    net = initFeatureExtractor()
    transformer = setTransformer(net)

    img = cv2.imread('test1.jpg')
    feature  = extractFeature(net, transformer, img)
    # print feature.shape
    
    simi = 1 - pw.pairwise_distances(feature, feature, metric='cosine')
    print simi
    print 'max simi:', np.max(simi)
    # simi = cos_dist(feature[0], feature[0])
    # print simi

if __name__ == '__main__':
    main()
