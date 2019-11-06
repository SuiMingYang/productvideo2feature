from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
from cv2 import cv2
import os

def model_cut(path):
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    #path=r"./image" #文件路径
    filelist = sorted(os.listdir(path),key=lambda x: int(x[:-4])) #该文件夹下的所有文件
    status=[]
    # loop over the image paths
    for imagePath in filelist:
        if imagePath=='.DS_Store':
            continue
        else:
            # load the image and resize it to (1) reduce detection time
            # and (2) improve detection accuracy
            image = cv2.imread(path+'/'+imagePath)
            image = imutils.resize(image, width=min(400, image.shape[1]))
            orig = image.copy()

            # detect people in the image
            (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                padding=(8, 8), scale=1.05)

            # draw the original bounding boxes
            for (x, y, w, h) in rects:
                cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # apply non-maxima suppression to the bounding boxes using a
            # fairly large overlap threshold to try to maintain overlapping
            # boxes that are still people
            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

            # draw the final bounding boxes
            for (xA, yA, xB, yB) in pick:
                cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

            # show some information on the number of bounding boxes
            filename = imagePath[imagePath.rfind("/") + 1:]
            print("[INFO] {}: {} original boxes, {} after suppression".format(
                filename, len(rects), len(pick)))
            
            if len(rects)!=0 and len(pick)!=0:
                status.append(1)
            else:
                status.append(0)
            # show the output images
            # cv2.imshow("Before NMS", orig)
            # cv2.moveWindow("trans:"+filename,500,0)
            # cv2.imshow("After NMS", image)
            # cv2.waitKey(1)
    return len(filelist),status




