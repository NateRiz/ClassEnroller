from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from file_manager import log

class I:
    _options = Options()
    #_options.add_argument("--headless")
    _options.add_argument("--disable-gpu")
    _driver = webdriver.Chrome(chrome_options = _options)

    @staticmethod
    def go_to_url(self, url):
        self.driver.get(url)

    @staticmethod
    def should_see(self, text):
        xpath = "//*[contains(text(),'{}')]"
        try:
            results = WebDriverWait(self.driver, 30).until(
                    self.driver.find_elements_by_xpath(xpath))
                 
        except Exception as e:
            log("should_see timeout for text: {} --- Error: {}".format(text, e))
            return False

        if not len(results):
            log("should_see: no results for {}".format(text))
            return False
        
        return True
            

