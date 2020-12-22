from video2graph import video_cut_pic
from peopleRecognition import model_cut
from face import dect_face
from taobao_api import taobao_pic_recognize
import numpy as np
import math
import time
from config import conf
from graph2video import function

if __name__ == "__main__":
    config='CONFIG'

    video_url=conf.get(config,"video_url")
    pic_url=conf.get(config,"pic_url")
    pic_type=conf.get(config,"pic_type")
    cookie=conf.get(config,"cookie")

    video_time_len,fps = video_cut_pic(video_url,pic_url,pic_type)
    #pic_len,status = model_cut(pic_url)
    pic_len,status = dect_face(pic_url)
    function(video_url,pic_url,pic_type)

    # cut_point=[]
    # pic_count=[]
    # change=0
    # for i in range(len(status)-2):
    #     if status[i]!=status[i+1]:
    #         change=1
    #     else:
    #         change=0
        
    #     if status[i]==0 and change==1:
    #         cut_point.append(i)
    #     elif i==0 and status[i]==1:
    #         cut_point.append(i)
    #     else:
    #         pass
        
    # for i in range(len(cut_point)-2):
    #     pic_count.append(round((cut_point[i]+cut_point[i+1])/2,0)+1)

    # cut_point=(np.array(cut_point)+1)/pic_len*video_time_len
    # print('视频截取点',cut_point)

    # for i in pic_count:
    #     # 请求淘宝接口
    #     # 用每个视频截断的中位数搜索商品
    #     taobao_pic_recognize(pic_url,str(math.floor(i))+pic_type,cookie)
    #     time.sleep(3)





