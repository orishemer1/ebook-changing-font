# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import os
import glob
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv


def get_info():
    link = "https://wordpress.org/showcase/archives/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)
    link_list = driver.find_elements(by=By.CLASS_NAME, value="storycontent")
    link_names = [l.text for l in link_list]
    temp_list = []
    print(len(link_names))
    for i in range(369, 390):
        try:
            l = link_names[i]
            temp = driver.find_element(by=By.PARTIAL_LINK_TEXT, value=l).click()
            print('*******page:', l.split()[0], i)
            xpath = f'(//div[@class="storycontent"]/a)'
            temp1 = driver.find_element(by=By.XPATH, value=xpath)
            temp1.click()
            try:
                elements = driver.find_elements(by=By.XPATH, value="//p")

                for elm in elements:
                    cssValue = elm.value_of_css_property("font-family")
                    table_dict = {'Font': cssValue, 'Text': elm.text}
                    temp_list.append(table_dict)
                df = pd.DataFrame(temp_list)



            except:
                print('problem')
                exit(-1)
            driver.back()
            driver.back()
        except:
            print('error')
    df.to_csv('table12.csv')


def get_info2():
    link = 'https://www.designbombs.com/best-weebly-websites-examples/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)
    list = ['https://www.wenxinwendyju.com/"']
    try:
        link_list = driver.find_elements(by=By.CLASS_NAME, value="post-stitle")
        for i in link_list: print(i.find_element(by=By.PARTIAL_LINK_TEXT, value='').text)
    except:
        print('no')


def merge_files():
    files = os.path.join("/Users/orishemer/PycharmProjects/ml_as_tool_ex_1", "table*.csv")

    # list of merged files returned
    files = glob.glob(files)
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    df.to_csv('output.csv')


get_info2()
# merge_files()
