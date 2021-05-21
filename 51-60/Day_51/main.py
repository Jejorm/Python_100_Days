from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 5000 # Change this.
PROMISED_UP = 5000  # Change this.
CHROME_DRVER_PATH = "yourchromedriver/path" # Change this.
TWITTER_EMAIL = "yourtwitter@mail.com" # Change this.
TWITTER_PASS = "yourtwitterpassword" # Change this.


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRVER_PATH)
        self.down = 0
        self.up = 0
        self.ping = 0
        self.tweet = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(2)

        self.test_button = self.driver.find_element_by_class_name("start-text")
        self.test_button.click()

        # Change this depending on how long the test takes
        sleep(40)

        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        self.ping = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)

    def tweet_at_provider(self):

        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
    
            self.driver.get("https://twitter.com/")

            self.tweet += f"Hey Internet Provider!, why is my Internet speed {self.down} down / {self.up} up. When I pay for {PROMISED_DOWN} down / {PROMISED_UP} up."

            sleep(2)

            twitter_login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
            twitter_login_button.click()

            sleep(2)

            twitter_login_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            twitter_login_input.send_keys(TWITTER_EMAIL)

            twitter_password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            twitter_password_input.send_keys(TWITTER_PASS)
            twitter_password_input.send_keys(Keys.ENTER)

            sleep(2)

            tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            tweet_input.click()
            tweet_input.send_keys(self.tweet)

            sleep(2)

            tweet_send_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_send_button.click()

            print(self.tweet)

        else:
            print("All OK!")

    def __str__(self) -> str:
        test = f"Down: {self.down}\nUp: {self.up}\nPing: {self.ping}"

        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            return f"{test}\n\n{self.tweet}"

        else:

            return f"{test}\n\nYour ISP is not that bad apparently."


a_object = InternetSpeedTwitterBot()

a_object.get_internet_speed()
a_object.tweet_at_provider()

print(a_object)
