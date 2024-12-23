# page_objects/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://example.com/login"  # 替换为实际URL

        # 元素定位器
        self.username_input = (By.ID, "username")  # 替换为实际的ID或选择器
        self.password_input = (By.ID, "password")  # 替换为实际的ID或选择器
        self.login_button = (By.ID, "login")        # 替换为实际的ID或选择器
        self.error_message = (By.ID, "error")       # 登录错误消息的定位器

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
    
    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
