from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # Считываем значение переменной x и вычисляем значение функции
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)
    print(answer)

    # Вводим полученный результат в поле
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)

    # Отмечаем чек-бокс
    checkbox = browser.find_element_by_id("robotCheckbox").click()

    # Ищим элемент radiobutton, проскроливаем к нему страницу и отмечаем
    radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
