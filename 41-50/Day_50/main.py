from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_MAIL = "fbemail@example.com"
FB_PASS = "facebookpassword"

CHROME_DRVER_PATH = "chromedriver/path" 
driver = webdriver.Chrome(executable_path=CHROME_DRVER_PATH)

driver.get("https://tinder.com")

sleep(2)
login_button = driver.find_element_by_css_selector("div .button")
login_button.click()

sleep(2)
fb_login_button = driver.find_element_by_xpath('//*[@id="q930268116"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login_button.click()

sleep(2)

tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

fb_email_input = driver.find_element_by_id("email")
fb_email_input.send_keys(FB_MAIL)

fb_password_input = driver.find_element_by_id("pass")
fb_password_input.send_keys(FB_PASS)
fb_password_input.send_keys(Keys.ENTER)

driver.switch_to.window(tinder_window)

sleep(2)

allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    sleep(1)

    try:
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:

        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

    #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
