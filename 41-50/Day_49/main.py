from selenium import webdriver
from time import sleep


CHROME_DRIVER_PATH = "chrome_driver_path"

LINKEDIN_EMAIL = "linkedinemail@example.com"
LINKEDIN_PASSWORD = "linkedinpassword"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=92000001&keywords=Web%20Developer&location=Remote")

sign_button = driver.find_element_by_css_selector("div .nav__button-secondary")
sign_button.click()

email_sign_button = driver.find_element_by_id("username")
sleep(1)
email_sign_button.send_keys(LINKEDIN_EMAIL)

password_sign_button = driver.find_element_by_id("password")
password_sign_button.send_keys(LINKEDIN_PASSWORD)

login_button = driver.find_element_by_css_selector("div button")
login_button.click()

sleep(3)

hide_msg = driver.find_elements_by_class_name("msg-overlay-bubble-header__control")[1]
hide_msg.click()

sleep(2)

jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in jobs:
    job.click()

    sleep(3)

    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()

print("All jobs saved")
