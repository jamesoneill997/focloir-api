from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

def init():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options) 
   
    return driver

def login():
    driver = init()
    username = 'ALM-translator8'
    pw = 'Asset_2021'
    url = 'https://cloud.memsource.com/web/login/auth?format_='
    
    driver.get(url)
    username_input_field = driver.find_element(By.ID, 'username')
    pw_input_field = driver.find_element(By.ID, 'password')
    submission_button = driver.find_element(By.ID, 'submit')

    username_input_field.send_keys(username)
    pw_input_field.send_keys(pw)
    submission_button.click()

    return

def scrape_terms():
    return

def write_terms():
    return

def main():
    login()

if __name__ == '__main__':
    main()