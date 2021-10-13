from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # Считываем значение переменной x
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")

    # Вычисляем функцию
    y = calc(x)

    # Вставляем значение функции в поле ввода
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отмечаем чек-бокс
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    # Отмечаем radiobutton
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
