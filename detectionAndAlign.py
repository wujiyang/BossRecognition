#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: wujiyang
@date: 2018-01-31
@brief: use mtcnn.py to do face detection and face alignment work. 
'''

import cv2
import sys
import math
import mtcnn

def faceAlign(input_image, points, output_size = (96, 112), ec_mc_y = 40):
    '''
    return the size-fixed align image with the given facial landmarks 
    '''
    allAlignFaces = []
    for i in range(points.shape[0]):
        '''
        points examples, which is different with happynear's examples
        [[219.68787 281.90543 244.70497 239.8125  293.89606]
         [155.76303 135.53867 185.15842 228.07518 212.40016]]
        '''
        if points.shape[1] == 10:
            currentPoints = points[i].reshape(2,5)
            # print currentPoints
        
            eye_center = ((currentPoints[0][0] + currentPoints[0][1]) / 2, (currentPoints[1][0] + currentPoints[1][1]) / 2)
            mouth_center = ((currentPoints[0][3] + currentPoints[0][4]) / 2, (currentPoints[1][3] + currentPoints[1][4]) / 2)
            angle = math.atan2(mouth_center[0] - eye_center[0], mouth_center[1] - eye_center[1]) / math.pi * -180.0
            scale = ec_mc_y / math.sqrt((mouth_center[0] - eye_center[0])**2 + (mouth_center[1] - eye_center[1])**2)
            center = ((currentPoints[0][0] + currentPoints[0][1] + currentPoints[0][3] + currentPoints[0][4]) / 4, 
                      (currentPoints[1][0] + currentPoints[1][1] + currentPoints[1][3] + currentPoints[1][4]) / 4)
            rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
            rot_mat[0][2] -= (center[0] - output_size[0] / 2)
            rot_mat[1][2] -= (center[1] - output_size[1] / 2)
            warp_dst = cv2.warpAffine(input_image, rot_mat, output_size)
            allAlignFaces.append(warp_dst)
        else:
            # only store the images with 10 facial lamdmarks
            continue

    return allAlignFaces

def fac_detection_alignment(img, minsize, PNet, RNet, ONet, threshold, factor):
    '''
    return all the aligned faces with the given image
    '''
    

    # face detection
    boundingboxes, points = mtcnn.detect_face(img, minsize, PNet, RNet, ONet, threshold, False, factor)

    # face alignment
    alignfaces = faceAlign(img, points)

    return alignfaces


def main():
    '''
    function test
    '''
    # model initialization, only do once !
    minsize, PNet, RNet, ONet, threshold, factor = mtcnn.initFaceDetector()

    # read image
    img = cv2.imread('test1.jpg')
    alignfaces = fac_detection_alignment(img, minsize, PNet, RNet, ONet, threshold, factor)

    for i in range(len(alignfaces)):
        cv2.imshow('img', alignfaces[i])
        cv2.waitKey()
   

if __name__ == "__main__":
    main()