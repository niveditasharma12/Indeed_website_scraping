from selenium import webdriver
import pandas as pd
import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class IndeedJob:
    def __init__(self, position, location, page):
        self.position=position
        self.location=location
        self.page=page

    def execute(self):
            lis = []
            os.environ['PATH'] += R";C:\seleniumDriver"
            driver = webdriver.Chrome()
            driver.get(f"https://in.indeed.com/jobs?q={self.position}&l={self.location}&start={self.page}")
            all_jobs = driver.find_elements(By.CLASS_NAME, 'result')
            for job in all_jobs:

                result_html = job.get_attribute('innerHTML')
                soup = BeautifulSoup(result_html, 'html.parser')
            # print(soup)
                try:
                    title = soup.find(class_="jobTitle").text.replace('\n', '')
            # title.click()
                except:
                    title = None
                try:
                    companyName = soup.find(class_="companyName").text.replace('\n', '').strip()
                except:
                    companyName = None
                try:
                    companyLocation = soup.find(class_="companyLocation").text.replace('\n', '').strip()
                except:
                    companyLocation = None
                try:
                    job_bugdet = soup.find(class_="attribute_snippet").text.replace('\n', '').strip()
                except:
                    job_bugdet = None
                try:
                    job_desc = soup.find(class_='job-snippet').text.replace('\n', '').strip()
                except:
                    job_desc = None

                lis.append({'Title': title, 'companyName': companyName, 'companyLocation': companyLocation,
                        'description': job_desc, 'job_budget': job_bugdet})
            return lis
a=IndeedJob("java","india",0)
n=a.execute()
print(n)




