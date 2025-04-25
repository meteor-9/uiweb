import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASEPATH)

#用例的路径
CASEPATH = os.path.join(BASEPATH,'test_case')
# print(CASEPATH)


#报告的路径和文件名
REPORTFILE = os.path.join(BASEPATH,'report','report.html')

#错误截图的路径
WEBPICTUREPATH = os.path.join(BASEPATH,'report','picture','')
# print(WEBPICTUREPATH)
