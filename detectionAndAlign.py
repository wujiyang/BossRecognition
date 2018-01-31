#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: wujiyang
@date: 2018-01-31
@brief: this file is for face detection and face alignment with the MTCNN models. 
        All models are released in the repository of MTCNN's official repository.
        https://github.com/kpzhang93/MTCNN_face_detection_alignment
'''
import cv2
import sys

detection_model_dir = '/home/wujiyang/face-verification/tools/MTCNN/code/codes/MTCNNv2/model/'

CascadeCNN = CascadeFaceDetection.CascadeCNN(model_folder + "det1-memory.prototxt", model_folder + "det1.caffemodel",
                     model_folder + "det1-memory-stitch.prototxt", model_folder + "det1.caffemodel",
                     model_folder + "det2-memory.prototxt", model_folder + "det2.caffemodel",
                     model_folder + "det3-memory.prototxt", model_folder + "det3.caffemodel",
                     model_folder + "det4-memory.prototxt", model_folder + "det4.caffemodel",
                     0) # 0 means to use the first gpu, -1 means to use cpu.

def fac_detection_alignment():
    pass














if __name__ == "__main__":
    pass