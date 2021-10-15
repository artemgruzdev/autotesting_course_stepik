from selenium import webdriver
import unittest


class CheckingRequiredInputFields(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fillForm(self, link):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Ivanov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.test")

        browser.find_element_by_css_selector("button.btn").click()

        welcome_text = browser.find_element_by_tag_name("h1").text
        return welcome_text

    def test_successfully(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fillForm(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_falls(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fillForm(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)


if __name__ == "__main__":
    unittest.main()
