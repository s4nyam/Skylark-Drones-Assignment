
from selenium import webdriver
# driver = webdriver.Firefox()
chromedriver = "/home/superuser/Desktop/skylark/template/chromedriver"
# driver.get("localhost:8000")
driver = webdriver.Chrome(chromedriver)
driver.get("localhost:8000")