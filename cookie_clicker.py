from selenium import webdriver
import time
import re

chrome_driver = 'D:\Application\Chrome Driver\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

time_start = time.time()
curr_time = time.time()
timeout = 300


def buy_item(idx):
    store = driver.find_elements_by_css_selector('#store b')

    buy_the_item = store[idx]
    print(buy_the_item.text)
    buy_the_item.click()


def format_str_into_int():
    store = driver.find_elements_by_css_selector('#store b')

    store.pop(-1)

    str_store = [int(re.sub('[^0-9]', '', store[x].text)) for x in range(len(store))]

    return str_store


def check_price(money, x):
    number_list = x
    idx = 0
    print(money)
    for i in range(len(number_list)):
        if money > number_list[i]:
            idx = i
    buy_item(idx)


def click_cookie():
    cookie_click = driver.find_element_by_xpath('//*[@id="cookie"]')
    cookie_click.click()


while time.time() < time_start + timeout:
    if round(time.time() - curr_time) == 5:
        curr_time = time.time()

        formatted_number = format_str_into_int()

        money_value = int(driver.find_element_by_id('money').text.replace(',', ''))

        check_price(money_value, formatted_number)
    click_cookie()
    # time.sleep(0.25)

driver.quit()
