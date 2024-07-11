from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import logging
import os

log_dir = "C:\\Users\\vishal\\PycharmProjects\\pythonProject"
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, 'test_log.txt')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    handlers=[
                        logging.FileHandler(log_filename),
                        logging.StreamHandler()
                    ])

service = Service("c:\\browserdrivers\\geckodriver.exe")
driver = webdriver.Firefox(service=service)
username = ""  #fill your username
password = ""  #fill your password

url = "https://www.atg.party"

driver.find_element(By.CLASS_NAME, "login-link").click()
logging.info("click login")
driver.find_element(By.ID, "email_landing").send_keys(username)
logging.info("fill username")
driver.find_element(By.ID, "password_landing").send_keys(password)
logging.info("fill password")
driver.find_element(By.CLASS_NAME, "landing-signin-btn").click()
logging.info("clicked submit button")

driver.get("https://www.atg.party/article")
logging.info("change url to atg.party/article")
driver.find_element(By.NAME, "title").send_keys("sample title")
logging.info("write title")
driver.find_element(By.CLASS_NAME, "ce-paragraph").send_keys("sample description")
logging.info("write description")
driver.find_element(By.ID, "cover_image").send_keys("c:\\browserdrivers\\cover.jpg")
logging.info("add cover image")
time.sleep(4)
logging.info("waiting for image to upload")
driver.find_element(By.ID, "hpost_btn").click()
logging.info("published the article")
