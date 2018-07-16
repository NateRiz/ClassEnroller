from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from file_manager import log
from course import Course

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
            select = Select(I._driver.find_element_by_id("MainContent_ddlSubject"))
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
    
    @staticmethod
    def check_for_space_in_section(section):
        courses = I._get_course_data(section)
        for c in courses:
            if section == None or c.section == section:
                if c.enrolled < c.limit:
                    log("SUCCESS: Found room in section {}.".format(section)


    @staticmethod
    def _get_sections(section):
        try:
            WebDriverWait(I._driver, 30).until(EC.presence_of_element_located((By.Class,"section-number")))
            sections = I._driver.find_elements_by_class("section_number")
            return [int(s.text()) for s in sections]
        except Exception as e:
            log("verify_section_exists error with passed in section: {} --- Error: {}".format(section, e))
            return list()

    @staticmethod
    def _get_enrolled():
        try:
            WebDriverWait(I._driver, 30).until(EC.presence_of_element_located((By.Class,"enrolled-currently")))
            enrolled = I._driver.find_elements_by_class("enrolled-currently")
            return [int(e.text()) for e in enrolled]
        except Exception as e:
            log("get_enrolled error --- Error: {}".format(e))
            return []

    @staticmethod
    def _get_limits()
        try:
            WebDriverWait(I._driver, 30).until(EC.presence_of_element_located((By.Class,"enrollment-limit")))
            limits = I._driver.find_elements_by_class("enrollment-limit")
            return [int(i.text()) for i in limits]
        except Exception as e:
            log("get_limits error --- Error: {}".format(e))
            return []

    @staticmethod
    def _get_course_data(section):
        sections = I._get_sections(section)
        enrolled = I._get_enrolled()
        limits = I._get_limits()
        if not(len(sections) == len(enrolled) == len(limits)):
            log("get_section_data data has uneven lengths. sections: {}, enrolled: {}, limits: {}".format(len(sections, len(enrolled, len(limits)))
            return
        courses = list()
        for i in range(len(sections):
            courses.append(Course(sections[i], enrolled[i], limits[i]))
        if len(courses) == 0:
            log("get_section_data no courses found.")
        return courses
