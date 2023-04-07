from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Demo_Class:

    #her testten once
    def setup_method(self):
        options = Options()
        options.page_load_strategy = 'normal'
        chrome_driver = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(chrome_driver, options=options)
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    #her testten sonra
    def teardown_method(self):
        self.driver.quit()

    def read_data(self):
        print("data read")

    def test_valid_login(self):  
        WebDriverWait(driver=self.driver, timeout=5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username_input = self.driver.find_element(By.ID,"user-name")
        password_input = self.driver.find_element(By.ID,"password")
      
       
        #ACTION CHAINS
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(username_input, "standard_user")
        actions.send_keys_to_element(password_input, "secret_sauce")
        actions.perform()
        login_click = self.driver.find_element(By.ID,"login-button").click()

        #JAVASCRIPT -> execute_script(JS comes here)
        # self.driver.execute_script('window.scrollTo(0,500)')

        message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        assert message.text == "Epic sadface: Username and password do not match any user in this service"
        

    def test_invalid_login(self):
        WebDriverWait(driver=self.driver, timeout=5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username_input = self.driver.find_element(By.ID,"user-name").send_keys("1")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password_input = self.driver.find_element(By.ID,"password").send_keys("1")
        login_click = self.driver.find_element(By.ID,"login-button").click()
        
        message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        assert message.text == "Epic sadface: Username and password do not match any user in this service"
        