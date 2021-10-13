from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    # Получаем число 1 и число 2 и вычесляем сумму
    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text
    answer = str(int(number1) + int(number2))

    # Ищим в выпадающем списке ответ и выбираем его
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(answer)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
