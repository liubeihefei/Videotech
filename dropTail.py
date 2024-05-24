"""
@FileName：dropTail.py
@Description：
@Author：liubeihefei
@Time：2024/5/23 22:46
"""

import os
import cv2 as cv


def getImageFiles(dir, formats):
    """
    根据视频地址与所需要的格式返回符合需要的视频绝对路径（暂时只支持视频都在同一父目录下一级的情况）
    :param dir:视频所在地址
    :param formats:后缀，为字符串列表
    :return:符合需要的视频绝对路径
    """
    files = os.listdir(dir)
    output = []
    # 遍历文件名
    for file in files:
        name, suf = file.split(".")

        # 判断后缀是否符合需求
        flag = False
        for fm in formats:
            if suf == fm:
                flag = True
                break

        # 若符合需求，则加入返回的文件绝对路径列表
        if flag:
            output.append(os.path.join(dir, file))

    return output


def dropTail(files, tail):
    """
    丢弃文件名中的tail尾巴
    :param files:文件绝对路径的字符串列表
    :param tail:想要丢弃的尾部部分的字符个数
    :return:无
    """
    for file in files:
        # 将原名取出
        name, suf = file.split(".")
        # 丢弃尾部取新名
        newname = name[:-tail]
        # 对文件重命名
        os.rename(file, newname + "." + suf)


if __name__ == '__main__':
    dropTail(getImageFiles("E:\影视资源\神奇宝贝\S02 宝可梦 超世代", ["mp4"]), 8)