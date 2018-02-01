# BossRecognition
识别靠近的Boss，并将桌面切换至工作区  

## Backgrounds  
近期把位置挪到实验室的角落以后，背对门的方向让我很没有安全感。万一老板突然查岗怎么办？哈哈哈，突然想到以前看的博客，做一个老板识别系统并实现桌面程序的秒切。我也来试试。

## Declaration 
这个小项目中用到的检测识别算法都来自于github上的开源项目，与实验室自己的人脸识别项目算法无关。  

All the face detection and face recognition algorithms used in this little project are from the open source community:github, which have none bussiness with my lab's face recognition projects.  

## Models  
FaceDetection Models: [MTCNN Models](https://github.com/kpzhang93/MTCNN_face_detection_alignment)  
FaceRecognition Model: []()   

## Architecture   
1. **_init_paths.py**: add cafffe to pythonpath.  
2. **mtcnn.py**: MTCNN implemention in python code.  
3. **detectionAndAlign.py**: return all the aligned faces when given an image. 
4. **extractFeature.py**: extract the face feature with an aligned face image.  


## Usage  
Runtime environment: Ubuntu 16.04.3 LTS with GPU of Geforce GTX 1080Ti


## Reference Codes  
1. [happynear/MTCNN_face_detection_alignment](https://github.com/happynear/MTCNN_face_detection_alignment)  
2. MTCNN with Python code: [DuinoDu/mtcnn](https://github.com/DuinoDu/mtcnn)