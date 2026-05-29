from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SocialMediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.instagram = (By.CSS_SELECTOR, "#col-1973173529 > div > div > div:nth-child(1) > a")
        self.telegram = (By.CSS_SELECTOR, "#col-1973173529 > div > div > div:nth-child(2) > a")
        self.facebook = (By.CSS_SELECTOR, "#col-1973173529 > div > div > div:nth-child(3) > a")
        self.youtube = (By.CSS_SELECTOR, "#col-1973173529 > div > div > div:nth-child(4) > a")
        self.linkedin = (By.CSS_SELECTOR, "#col-1973173529 > div > div > div:nth-child(5) > a")

    def click_logo_instagram(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.instagram))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_logo_telegram(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.telegram))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_logo_facebook(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.facebook))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_logo_youtube(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.youtube))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_logo_linkedin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.linkedin))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_btn_back(self):
        # Вызываем встроенную команду истории браузера напрямую
        self.driver.execute_script("window.history.go(-1);")
