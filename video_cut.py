# 裁剪视频

import os
from cv2 import cv2
import math


def read_video():
    """
    获取到输入的视频路径，并建立保存的路径。
    :return:
    """
    #video_path = input(r'请输入视频的路径[eg：D:\Video\66.mp4]：')
    video_path='./测试.mp4'
    all_info = video_path.split('\\')
    file_name = all_info[-1].split('.')[0]
    save_path = '\\'.join(all_info[:-1]) + '\\data' + '\\' + file_name + '.avi'
    try:
        if not os.path.exists(save_path):
            os.mkdir('\\'.join(all_info[:-1]) + '\\data')
    except FileExistsError as e:
        print(u'保存路径已经创建......')
    return video_path, save_path


def clip_video():
    """
    对视频任意时间段进行剪切
    :return:
    """
    video_path, save_path = read_video()
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('video is not opened')
    else:
        success, frame = cap.read()
        f_shape = frame.shape
        f_height = f_shape[0]  # 原视频图片的高度
        f_width = f_shape[1]
        fps = cap.get(5)  # 帧速率
        frame_number = cap.get(7)  # 视频文件的帧数
        duration = frame_number / fps  # 视频总帧数/帧速率 是时间/秒【总共有多少秒的视频时间】
        print('请注意视频的总时间长度为 %s 秒' % str(duration))
        start = input('请输入开始时间/秒为单位 例如输入：0[代表从第 0 秒开始剪切]：')
        while True:
            if int(start) > int(math.ceil(duration)):
                start = input('输入结束时间大于总视频时间请重新输入......时间：')
            else:
                break
        start_time = fps * float(start)
        end = input('请输入结束时间/秒为单位 例如输入：10[代表到第 10 秒结束剪切]')
        while True:
            if int(end) > int(math.ceil(duration)):
                end = input('输入结束时间大于总视频时间请重新输入......时间：')
            else:
                break
        end_time = fps * float(end)
        # AVI格式编码输出 XVID
        # 编码格式可修改，键值对
        four_cc = cv2.VideoWriter_fourcc(*'XVID')
        video_writer = cv2.VideoWriter(save_path, four_cc, fps, (int(f_width), int(f_height)))
        num = 0
        while True:
            success, frame = cap.read()
            if int(start_time) <= int(num) <= int(end_time):
                if success:
                    video_writer.write(frame)
                else:
                    break
            num += 1
            if num > frame_number:
                break
        cap.release()


if __name__ == '__main__':
    clip_video()


'''
# 图像合成视频
import os
from cv2 import cv2
import uuid


def read_picture():
    #path = input('请输入视频的路径[eg：D:\Image\BaiDuImgDownLoad\liuhai]: ')
    path='image'
    file_list = os.listdir(path)

    fps = input('请输入视频的帧速率，秒为单位，一秒播放多少张照片：')  # 视频每秒2帧
    height = input('请输入视频图片尺寸的高度，视频的高清程序')
    weight = input('请输入视频图片尺寸的宽度，视频的高清程序')
    size = (int(height), int(weight))  # 需要转为视频的图片的尺寸
    return [path, fps, size, file_list]


def write_video():
    path, fps, size, file_list = read_picture()
    # AVI格式编码输出 XVID
    four_cc = cv2.VideoWriter_fourcc(*'XVID')
    save_path = path + '\\' + '%s.avi' % str(uuid.uuid1())
    video_writer = cv2.VideoWriter(save_path, four_cc, float(fps), size)
    # 视频保存在当前目录下
    for item in file_list:
        if item.endswith('.jpg') or item.endswith('.png'):
            # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
            item = path + '\\' + item
            img = cv2.imread(item)
            re_pics = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)  # 定尺寸
            if re_pics:
                video_writer.write(re_pics)

    video_writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    write_video()
'''

