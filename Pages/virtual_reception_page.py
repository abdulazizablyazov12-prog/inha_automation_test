from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class VirtualReception:
    def __init__(self, driver):
        self.driver = driver
        self.reception_page = (By.CSS_SELECTOR, "#wide-nav > div > div.flex-col.hide-for-medium.flex-right.flex-grow > ul > li.html.header-button-1 > div > a")
        self.full_name = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(2) > label > span > input")
        self.region = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(3) > label > span > input")
        self.city = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(4) > label > span > input")
        self.address = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(5) > label > span > input")
        self.age = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(6) > label > span > input")
        self.email = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(7) > label > span > input")
        self.phone_number = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(8) > label > span > input")
        self.text = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(9) > label > span > textarea")
        self.btn_submit = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > p:nth-child(10) > input")
        self.submitted_msg = (By.CSS_SELECTOR, "#wpcf7-f5650-p5643-o1 > form > div.wpcf7-response-output")
        self.btn_language = (By.CSS_SELECTOR, "#wide-nav > div > div.flex-col.hide-for-medium.flex-right.flex-grow > ul > li.has-dropdown.header-language-dropdown")
        self.uz_language = (By.CSS_SELECTOR, "#wide-nav > div > div.flex-col.hide-for-medium.flex-right.flex-grow > ul > li.has-dropdown.header-language-dropdown > ul > li:nth-child(3) > a")

    def click_reception_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.reception_page)).click()

    def input_full_name(self, full_name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.full_name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(full_name)

    def input_region(self, region):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.region))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(region)

    def input_city(self, city):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.city))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(city)

    def input_address(self, address):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.address))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(address)

    def input_age(self, age):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.age))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(age)

    def input_email(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.email))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(email)

    def input_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.phone_number))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(phone_number)

    def input_text(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.text))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.send_keys(text)

    def click_btn_submit(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.btn_submit))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_submitted_msg(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.submitted_msg))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_btn_language(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.btn_language))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_uz_language(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.uz_language)).click()