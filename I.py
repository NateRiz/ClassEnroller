from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from file_manager import log

class I:
    def __init__(self):
        self.driver = webdriver.FirefoxProfile()

    def __del__(self):
        pass
        #None of these work...
        #self.driver.kill()
        #self.driver.close()
        #self.driver.quit()
        



    def go_to_url(self, url):
        self.driver.get(url)


    def should_see(self, text):
        xpath = "//*[contains(text(),'{}')]"
        try:
            results = WebDriverWait(self.driver, 30).until(
                    self.driver.find_elements_by_xpath(xpath)
                )
                 
        except Exception as e:
            log("should_see timeout for text: {} --- Error: {}".format(text, e))
            return False

        if not len(results):
            log("should_see: no results for {}".format(text))
            return False
        
        return True
            

