"""
@FileName：turnFormat.py
@Description：
@Author：horsefly
@Time：2024/5/24 10:14
"""


from dropTail import getImageFiles
import cv2 as cv


def getFormat(file):
    """
    获取视频的编码格式
    :param file: 视频文件的绝对路径
    :return:丐版的编码格式信息
    """
    cap = cv.VideoCapture(file)
    codec = int(cap.get(cv.CAP_PROP_FOURCC))
    codec =chr(codec & 0xFF) + chr((codec >> 8) & 0xFF) + chr((codec >> 16) & 0xFF) + chr((codec >> 24) & 0xFF)
    return codec


def turnFromat(files, suf):
    """
    将视频格式更改为所需后缀对应的格式（更改好的视频将放在与原视频同样的目录下）
    :param files:文件的绝对路径，为字符串列表
    :param suf:想要的格式后缀，为字符串
    :return:无
    """
    # 遍历每个文件
    for file in files:
        cap = cv.VideoCapture(file)
        # 设置保存视频的各项信息
        name, _ = file.split(".")
        # codec = cv.VideoWriter.fourcc('H', '2', '6', '4');
        codec = cv.VideoWriter.fourcc(*'avc1');
        writer = cv.VideoWriter(name + "." + suf, codec, cap.get(cv.CAP_PROP_FPS),
            (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        # 遍历原视频每一帧，进行格式转换
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                writer.write(frame)
            else:
                break

if __name__ == "__main__":
    # print(getFormat("E:\影视资源\神奇宝贝\S01 宝可梦 无印\第126集 布卢的华丽生活.mp4"))
    turnFromat(["E:\影视资源\神奇宝贝\S01 宝可梦 无印\第001集 宠物小精灵 就决定是你了.rmvb"], "mp4")