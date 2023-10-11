# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Start the browser and login with standard_user
def login(driver, user, password):
    print('Starting the browser...')
    # login
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    productText = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in productText
    print('Login with username {user} and password {password} successfully.'.format(user=user, password=password))

def add_cart(driver):
    # driver = webdriver.Chrome()
    itemElements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for itemEle in itemElements:
        itemEle.find_element(By.CLASS_NAME, "btn_primary").click()
        itemName = itemEle.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(itemName + " added to shopping cart.")
    size = int(driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
    assert size == len(itemElements)
    print('{:d} items are all added to shopping cart successfully.'.format(size))

def remove_cart(driver):
    # driver = webdriver.Chrome()
    itemElements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for itemEle in itemElements:
        itemEle.find_element(By.CLASS_NAME, "btn_secondary").click()
        itemName = itemEle.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(itemName + " removed from shopping cart.")
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
    print('{:d} items are all removed from shopping cart successfully.'.format(len(itemElements)))


if __name__ == "__main__":
    NUM_ITEMS = 2
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    chromeOptions = ChromeOptions()
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument("--headless") 
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Chrome(options=chromeOptions)

    print('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    login(driver, USERNAME, PASSWORD)
    add_cart(driver)
    remove_cart(driver)
    print('Selenium tests are all successfully completed!')
    driver.close()
