from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce:
    def test_invalid_login(self):
        options = Options()
        options.page_load_strategy = 'normal'
        options.accept_insecure_certs = True
        chrome_driver = ChromeDriverManager().install()
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(3)
        username_input = driver.find_element(By.ID,"user-name").send_keys("1")
        password_input = driver.find_element(By.ID,"password").send_keys("1")
        login_click = driver.find_element(By.ID,"login-button").click()
        
        error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        test_result = error_message.text == "Epic sadface: Username and password do not match any user in this service"
        
        print(f"Result : {test_result}")
        

testClass = Test_Sauce()
testClass.test_invalid_login()
        
