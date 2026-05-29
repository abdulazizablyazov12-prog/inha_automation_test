from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UniversitetPage:
    def __init__(self, driver):
        self.driver = driver
        self.universitet_dropdown = (By.CSS_SELECTOR, "#menu-item-4672 > a")
        self.iut_haqida = (By.CSS_SELECTOR, "#col-2085045897 > div > ul:nth-child(2) > li:nth-child(1) > a")
        self.universitet_btn_back = (By.CSS_SELECTOR, "#breadcrumbs > span > span:nth-child(3) > a")
        self.rektor_haqida = (By.CSS_SELECTOR, "#col-2085045897 > div > ul:nth-child(4) > li:nth-child(1) > a")
        self.professorlar = (By.CSS_SELECTOR, "#col-2085045897 > div > ul:nth-child(8) > li:nth-child(1) > a")
        self.professor_card = (By.CSS_SELECTOR, "#image_476701550 > a > div")
        self.professor_card_exit = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-auto-cursor.mfp-ready > button")


    def click_universitet_dropdown(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.universitet_dropdown)).click()

    def click_iut_haqida(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.iut_haqida)).click()

    def click_universitet_btn_back(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.universitet_btn_back)).click()

    def click_rektor_haqida(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.rektor_haqida))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_professorlar(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.professorlar))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_professor_card(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.professor_card))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_professor_card_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.professor_card_exit)).click()





