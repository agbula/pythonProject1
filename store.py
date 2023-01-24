# Section B:
# 1.Automate Add 5 items to Cart, remove the item 1, 3 and 5
# 2.Continue shopping, add two more items
# 3.Checkout button
# 4.Automate Log out
# 5.Close browser


import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# website launch(https://www.saucedemo.com/)
driver.get("https://www.saucedemo.com/")

# Enter Login Credentials to login

driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Automate add 5 items to cart
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(5)

# Remove items 1, 3 and 5
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-onesie"]').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
time.sleep(5)


# Checkout
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(5)


# Continue Shopping
driver.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()


# add 2 more items
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
time.sleep(5)

# checkout
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').click()
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("olutola")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("agboola")
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("1000022")
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="continue"]').click()
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()

time.sleep(3)

# 4.Automate Log out
driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()









time.sleep(30)












