from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CHROME_DRVER_PATH = "chromedriver/path"
USERNAME = "yourinstagramusername"
PASSWORD = "youristagrampassword"
ACCOUNT_FOLLOW = "leomessi"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(2)

        login_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_input.send_keys(USERNAME)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get(f"https://instagram.com/{ACCOUNT_FOLLOW}")

        sleep(2)

        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()

        sleep(2)

        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)


    def follow(self):
        all_follow_buttons = self.driver.find_elements_by_css_selector("li button")

        for follow_button in all_follow_buttons:
            try:
                follow_button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_follow_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_follow_button.click()


instagram = InstaFollower(CHROME_DRVER_PATH)

instagram.login()
instagram.find_followers()
instagram.follow()