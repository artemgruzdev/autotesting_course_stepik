from selenium import webdriver
import time
import os


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Заполняем поля имя, фамилия, e-mail
    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Ivanov")
    e_mail = browser.find_element_by_name("email")
    e_mail.send_keys("test@test.test")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    element_download = browser.find_element_by_id("file")
    element_download.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
