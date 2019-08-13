#pip install selenium

from selenium import webdriver

# Call Chrome Driver
driver = webdriver.Chrome(executable_path="C:\\Users\\Idit\\PycharmProjects\\chromedriver.exe")
# wait for elements
driver.implicitly_wait(20)
# open website
driver.get('http://192.168.99.100:5000/')
#get all text in body
html = driver.page_source
print(html)
# quit webdiver
driver.quit()