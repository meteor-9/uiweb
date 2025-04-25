from time import sleep

from lib.pyse import Pyse
import time
from lib.tool import Tool
from PIL import Image
import cv2

'''
PageObject实际上就是
将一个页面   抽象成一个类  页面上可操作的元素 抽象成方法

'''
import pandas as pd


class BasePage(object):
    def __init__(self):
        self.pyse= Pyse('chrome')

    def open(self):
        self.pyse.open('https://www-pro.dongmayinzhang.com/znkf/')

    def quit(self):
        self.pyse.quit()

class QuestionPage(BasePage):

    def question(self,question):
        css = 'css=>#messageInput'
        self.pyse.type(css, question)
        css = 'css=>.send-btn'
        self.pyse.click(css)

    def checkstop(self):
        css = 'css=>.stop-btn'
        self.pyse.check_button(css)




# 这样继承下来，只需要实例化Page就都可以用了
class Page(QuestionPage):
    pass

def read_excel_column_to_list(file_path, start_row, end_row):
    """
    读取Excel文档中指定列的内容，保存到列表中。

    Args:
        file_path (str): Excel文件的路径。
        start_row (int): 开始读取的行号（从1开始计数）。
        end_row (int): 结束读取的行号。

    Returns:
        list: 包含读取内容的列表，如果出错则返回空列表。
    """

    try:
        df = pd.read_excel(file_path)  # 默认读取第一个sheet
        column_data = df.iloc[start_row - 1:end_row, 1]  # pandas 是 0-based index，列也是 0-based (第二列索引为1)
        data_list = column_data.astype(str).str.strip().tolist()  # 转换为字符串，去除空格，转为 list
        return data_list
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到。")
        return []
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return []


if __name__ == '__main__':
    excel_file = "/Users/gaometeor/Desktop/动码印章/ai测试问题.xlsx"  # 替换为你的Excel文件路径
    start_row = 1
    end_row = 75

    result = read_excel_column_to_list(excel_file, start_row, end_row)

    page = Page()
    page.open()
    for item in result:
        page.question(item)
        page.checkstop()
    # page.quit()
    # page = Page()
    # page.open()
    # page.question('asdfadf')
    # page.checkstop()




