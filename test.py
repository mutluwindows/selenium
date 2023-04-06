from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


options = Options()
options.page_load_strategy = 'normal'

chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome_driver, options=options)
driver.maximize_window()
driver.get("https://app.datacamp.com/learn/courses")

print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
sleep(15)
user_login = driver.find_element(By.ID, "user_email").send_keys("mutluwinddows@gmail.com")
driver.get("https://app.datacamp.com/learn/courses")
print(f"User Login : {user_login}")


input()
#HTML SELECTORS
 