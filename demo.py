#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: wujiyang
@date: 2018-02-01
@brief: a demo for face recognition
'''


import _init_paths
import mtcnn
import detectionAndAlign
import extractFeature
import cameraCapture
import processManage

import cv2
import os
import numpy as np
import sklearn.metrics.pairwise as pw

def dirList(path, allfiles):
    '''
    get all files with recursive way, saving the file paths to a result list
    '''
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirList(filepath, allfiles)
        else:
            allfiles.append(filepath)


def loadFaceLib(net, transformer, minsize, PNet, RNet, ONet, threshold, factor):
    '''
    extract the feature of someone who you want to recognize
    put some images of the one you want to recognize to the folder ./images/ 
    '''
    libPath = './images/'
    allperson = []
    dirList(libPath, allperson)
    libFeature = np.zeros((len(allperson), 512))
    for i in range(len(allperson)):
        img = cv2.imread(allperson[i])
        alignfaces, img = detectionAndAlign.fac_detection_alignment(img, minsize, PNet, RNet, ONet, threshold, factor)
        # in face lib , one image only has one face
        if len(alignfaces) >= 1:
            feature = extractFeature.extractFeature(net, transformer, alignfaces[0])
            libFeature[i] = feature[0]  

    return libFeature



def main():
    #--------------------------------------------------------
    # step 1: model initialization
    #--------------------------------------------------------
    minsize, PNet, RNet, ONet, threshold, factor = mtcnn.initFaceDetector()
    net = extractFeature.initFeatureExtractor()
    transformer = extractFeature.setTransformer(net)

    #--------------------------------------------------------
    # step 2: load facelib feature from lib folder
    #--------------------------------------------------------
    libFeature = loadFaceLib(net, transformer, minsize, PNet, RNet, ONet, threshold, factor)
    print libFeature.shape

    #--------------------------------------------------------
    # step 3: read image from camera and calculate similarity
    #--------------------------------------------------------
    cap = cv2.VideoCapture(0)
    while(1):
        frame = cameraCapture.getFrameFromCamera(cap)
        cv2.putText(frame, "press 'q' to exit", (10, 30), 0, 1, (255, 0, 0), 1, False)
        alignfaces, frame = detectionAndAlign.fac_detection_alignment(frame, minsize, PNet, RNet, ONet, threshold, factor)
        cv2.imshow('capture',frame)
        # cv2.imwrite('capture/'+str(j)+'.jpg', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            print 'welcome to use again, good bye~'
            break
            cv2.destroyAllWindows()
        # calculate the similarity
        for i in range(len(alignfaces)):
            feature  = extractFeature.extractFeature(net, transformer, alignfaces[i])
            simi = 1 - pw.pairwise_distances(libFeature, feature, metric='cosine')
            # print simi
            print 'max simi:', np.max(simi)
            if(np.max(simi) > 0.68):
                processManage.closeProcess()
                # processManage.openProcess()
                processManage.show_image()
        
    cap.release()


if __name__ == "__main__":
    main()

