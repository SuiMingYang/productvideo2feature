from cv2 import cv2
import os
import shutil

# 视频分帧截图
def video_cut_pic(video_name,pic_url,pic_type):
    cap = cv2.VideoCapture(video_name)
    success, frame = cap.read()
    f_shape = frame.shape
    f_height = f_shape[0]  # 原视频图片的高度
    f_width = f_shape[1]
    fps = cap.get(5)  # 帧速率
    frame_number = cap.get(7)  # 视频文件的帧数
    duration = frame_number / fps  # 视频总帧数/帧速率 是时间/秒【总共有多少秒的视频时间】
    print('视频的总时间长度为 %s 秒' % str(duration))

    shutil.rmtree(pic_url) #将整个文件夹删除

    os.makedirs(pic_url) #重新创建文件夹 
        
    vc = cv2.VideoCapture(video_name) #读入视频文件
    c=1
    i=1
    
    if vc.isOpened(): #判断是否正常打开
        rval , frame = vc.read()
    else:
        rval = False
    
    fps = round(fps/10,0)  #视频帧计数间隔频率
    
    while rval:   #循环读取视频帧
        rval, frame = vc.read()
        if c%fps == 0: #每隔timeF帧进行存储操作
            cv2.imwrite(pic_url+'/'+str(i) + pic_type,frame) #存储为图像
            i=i+1
        c = c + 1
        #cv2.waitKey(1)
    vc.release()
    return duration,fps

if __name__ == "__main__":
    video_cut_pic('./测试.mp4','./image','.jpg')
