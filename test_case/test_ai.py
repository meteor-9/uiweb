import time
import unittest
from page.aethir import Page

# ui自动化很少用到数据驱动，所以不需要参数化数据，只检查页面逻辑展示
class testAi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        cls.page.open()


    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_question(self):
        self.page.question()
        time.sleep(20)




if __name__ == '__main__':
    unittest.main()














