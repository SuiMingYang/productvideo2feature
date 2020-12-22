from cv2 import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# '''视频转图片'''
# cap=cv.VideoCapture('./测试.mp4') #加载视频
# isOpened=cap.isOpened()
# i=0
# 
# while(isOpened):
#     i=i+1
#     flag,frame=cap.read()
#     fileName = str(i)+".png"
#     print(fileName)
#     if flag == True :
#         cv.imwrite(str(i)+".png",frame) # 命名 图片 图片质量，此处文件名必须以图片格式结尾命名
#         cv.waitKey(1)
#     else:
#         break
# cap.release()
# print('end')

'''图片转视频'''
import os

def function(url,pic_url,pic_type):

    '''获取视频信息'''
    cap=cv.VideoCapture(url) # 加载视频
    fps=cap.get(cv.CAP_PROP_FPS) # 获取帧率
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) # 获取宽度
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) # 获取高度
    print(fps,width,height)
    path=pic_url

    filelist = os.listdir(path)
    filelist = sorted(os.listdir(path),key=lambda x: int(x[:-4])) #该文件夹下的所有文件

    size = (width, height) #需要转为视频的图片的尺寸
    video = cv.VideoWriter("./hecheng.avi", cv.VideoWriter_fourcc(*'MJPG'), fps, size)
    #video = cv.VideoWriter("./hecheng.mp4", cv.VideoWriter_fourcc(*'mp4v'), fps, size)
    # video = cv.VideoWriter("./hecheng.mp4", cv.VideoWriter_fourcc(*'avc1'), fps, size)
    for item in filelist:
        if item.endswith(pic_type): 
            #print(item)
            img = cv.imread(pic_url+'/'+item)
            video.write(img)

    video.release()
    cv.destroyAllWindows()
    print('end')

