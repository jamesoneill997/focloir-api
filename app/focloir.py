from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By


def init():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)  
    driver = webdriver.Chrome(chrome_options=chrome_options) 
   
    return driver

def search_term(driver, term):
    url = "https://www.focloir.ie/en/dictionary/ei/"
    formatted_term = format_term(term)
    driver.get(url+formatted_term)
    return

def format_term(term):
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


def main():
    driver = init()
    search_term(driver, 'game')
if __name__ == '__main__':
    main()
