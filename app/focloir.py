from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

class Focloir:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options) 
        self.driver = driver

    def search_term(self, term):
        driver = self.driver
        url = "https://www.focloir.ie/en/dictionary/ei/"
        formatted_term = self.format_term(term)
        driver.get(url+formatted_term)
        WebDriverWait(driver, timeout=15).until(ec.presence_of_element_located((By.CLASS_NAME, "sense")))
        print(self.get_translation())
        return

    def format_term(self, term):
        formatted_string = ""
        words = term.split(" ")
        #if only 1 word, formatting not needed
        if len(words) == 1:
            return term
        for word in words:
            if not words.index(word) == len(words) - 1:  #if it isn't the last word
                formatted_string = word + "+"
            else:
                formatted_string += word

        return formatted_string

    def get_translation(self):
        driver = self.driver
        results = driver.find_element(By.CLASS_NAME, 'cit_translation').text
        if "masc" in results.split(" ")[1] or "fem" in results.split(" ")[1]:
            return results.split(" ")[0]
        else:
            return results