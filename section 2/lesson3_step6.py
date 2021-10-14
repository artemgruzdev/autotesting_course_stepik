from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.trollface").click()

    # Переключаемся на новую вкладку браузера
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Получаем x и вычислаем значение функции
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)

    # Вводим ответ в поле ввода
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)

    # Отправляем заполненную форму
    button_end = browser.find_element_by_css_selector("button.btn")
    button_end.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
