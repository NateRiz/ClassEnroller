from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from file_manager import log

class I:
    _options = Options()
    _options.add_argument("--headless")
    _options.add_argument("--disable-gpu")
    _driver = webdriver.Chrome(chrome_options = _options)

    @staticmethod
    def go_to_url(url):
        I._driver.get(url)

    @staticmethod
    def search_for_course(subject, course_number = "*"):
        try:
            WebDriverWait(I._driver, 30).until(EC.presence_of_element_located((By.ID,"MainContent_ddlSubject")))
            select = Select(I._driver.find_elemnt_by_id("MainContent_ddlSubject"))
            select.select_by_value(subject.upper())
        except Exception as e:
            log("search_for_course Dropdown Select error with passed in subject: {}, course_number: {} --- Error: {}".format(subject,course_number, e))
            return
        try:
            field = I._driver.find_element_by_id("MainContent_txtCourseNumber")
            field.clear()
            field.send_keys(course_number)
        except Exception as e:
            log("search_for_course Field Fill error with passed in subject: {}, course_number: {} --- Error: {}".format(subject,course_number, e))
            return
        
        try:
            button = I._driver.fine_element_by_id("MainContent_btnSubmit")
            button.click()
        except Exception as e:
            log("search_for_course Button Click error with passed in subject: {}, course_number: {} --- Error: {}".format(subject, course_number, e))
            return

        I._driver.save_screenshot("img.png")

