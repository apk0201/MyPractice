from selenium import webdriver
from os.path import expanduser

home = expanduser("~")
driver = webdriver.Chrome(executable_path=home+r"\PycharmProjects\Selenium\AutomateAddingItemsToCart\driver"
                                               r"\\chromedriver.exe")
driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://www.amazon.com")
ele = driver.find_element_by_link_text("Books")
ele.click()
ele = driver.find_element_by_xpath("//a[@href = '/Childrens-Books/b/?ie=UTF8&node=4&ref_=sv_b_4']")
ele.click()
ele = driver.find_element_by_xpath("//a[@title = 'Education & Reference']")
ele.click()
ele = driver.find_element_by_id("twotabsearchtextbox")
ele.send_keys("Peppa pig")
ele = driver.find_element_by_xpath("//input[@value = 'Go']")
ele.click()
ele = driver.find_element_by_xpath("//div/img[@data-image-index='3']")
ele.click()
ele = driver.find_element_by_id("add-to-cart-button")
ele.click()
ele1 = driver.find_element_by_id("nav-cart-count")
txt = ele1.text
if int(txt) >= 1:
    ele1.click()
else:
    print("Item not added to cart. Please add again")
    ele.click()
driver.get_screenshot_as_file("screenshot.png")
driver.close()
