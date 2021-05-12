from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriverpath/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.amazon.com/-/es/identificadora-Stronghold-retr%C3%A1ctil-protector-resistente/dp/B07MF9KBF7/ref=bmx_4?pd_rd_w=s4Evy&pf_rd_p=b56a886c-2bb4-4e74-b4cf-23d7a76693c8&pf_rd_r=C5GC49Q5SS6R3C765YJ2&pd_rd_r=db0e568d-4a46-4b22-9d7c-e28818c9c6d4&pd_rd_wg=6xMIC&pd_rd_i=B07MF9KBF7&psc=1")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# driver.get("https://www.python.org/")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# # CHALLENGE!
# scraping = driver.find_elements_by_css_selector(".shrubbery .menu")
# events = scraping[1].text.splitlines()
# events_dict = {count: {"time": event[0], "name": event[1]} for count, event in enumerate(zip(events[::2], events[1::2]))}
# print(events_dict)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# # CHALLENGE!!
# driver.get("http://secure-retreat-92358.herokuapp.com/")

# f_name = driver.find_element_by_name("fName")
# f_name.send_keys("Name")

# l_name = driver.find_element_by_name("lName")
# l_name.send_keys("LastName")

# email = driver.find_element_by_name("email")
# email.send_keys("thsis@email.com")

# sign_up = driver.find_element_by_tag_name("button")
# sign_up.click()


# driver.close() # Close a tab
# driver.quit() # Close the program