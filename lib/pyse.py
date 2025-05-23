# coding=utf-8
import time
from audioop import reverse

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Pyse(object):
    '''
        Pyse framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    '''

    def __init__(self, browser='ff'):
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            option = webdriver.ChromeOptions()
            option.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=option)
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        elif browser == 'edge':
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def element_wait(self, css, secs=5):
        '''
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "find_elements":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):
        '''
        Judge element positioning way, and returns the element.
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.driver.find_element(By.ID, value)
        elif by == "name":
            element = self.driver.find_element(By.NAME, value)
        elif by == "class":
            element = self.driver.find_element(By.CLASS_NAME, value)
        elif by == "link_text":
            element = self.driver.find_element(By.LINK_TEXT, value)
        elif by == "xpath":
            element = self.driver.find_element(By.XPATH, value)
        elif by == "css":
            element = self.driver.find_element(By.CSS_SELECTOR,value)
        elif by == "find_elements":
            element = self.driver.find_elements(By.CSS_SELECTOR, value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        '''
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)

    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def type(self, css, text):
        '''
        Operation input box.

        Usage:
        driver.type("css=>#el","selenium")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def clearAll(self, css):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(Keys.CONTROL,"a")
        el.send_keys(Keys.DELETE)

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def click_onebyone(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        els = self.get_element(css)
        for el in reversed(els):
            el.click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def slider(self,slider,distance):
        '''
        Slide a slider to some distance.

        Usage:
        driver.slider("css=>#el","distance")
        '''
        # 创建动作链
        if distance is not None:
            actions = ActionChains(self.driver)
            # 按住滑块
            actions.click_and_hold(slider).perform()
            # 滑动到目标位置
            actions.move_by_offset(distance,0).perform()
            # 释放滑块
            actions.release().perform()
            time.sleep(5)
        else:
            print("拖拽位置不对！")

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.default_content()

    def switch_to_frame_parent(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.parent_frame()

    def open_new_window(self):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    # def _save_png(self, name):
    #     self.get_windows_img(name)

    def check_button(self, css):
        '''
        Get element text information.

        Usage:
        driver.check_button("css=>#el")
        '''
        while True:
            self.element_wait(css)
            el = self.get_element(css)
            result = el.get_attribute("style")
            if result == "display: none;":
                return True

    def save_screenshot(self,path):
        try:
            self.driver.save_screenshot(path)
        except Exception as e:
            print(e)

    def wait_and_save_exception(self, css, name):
        try:
            self.element_wait(css, secs=5)
            return True
        except Exception as e:
            from lib.path import WEBPICTUREPATH
            self.get_windows_img(WEBPICTUREPATH + name + '.png')
            return False

    def wait_and_exception(self, css):
        try:
            self.element_wait(css, secs=10)
            return True
        except Exception as e:
            return False

    def select_by_value(self, css, value):
        self.element_wait(css)
        el = self.get_element(css)
        Select(el).select_by_value(value)



if __name__ == '__main__':
    driver = Pyse("chrome")
