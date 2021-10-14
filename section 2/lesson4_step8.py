from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Ждем когда цена дома уменьшится до 100$ и жмем на кнопку
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book").click()

    # Скролим к элементу x, считываем, вычисляем формулу, вводим в поле ввода
    x_element = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    answer = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)

    # Отправляем заполненную форму
    button_end = browser.find_element_by_id("solve")
    button_end.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
