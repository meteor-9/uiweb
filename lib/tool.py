import os
from lib.path import WEBPICTUREPATH
import cv2
import numpy as np

class Tool(object):

    def error_picture(self):
        '''
        提供错误图片，
        :return:
        '''
        pictures = []
        files = os.listdir(WEBPICTUREPATH)
        for item in files:
            if item.endswith('.jpg') or item.endswith('.png'):
                pictures.append((item,))
        return pictures

if __name__ == '__main__':
    print(Tool().error_picture())

