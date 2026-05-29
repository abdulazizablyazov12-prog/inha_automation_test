from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TalabalarPage:
    def __init__(self, driver):
        self.driver = driver
        self.talabalar = (By.CSS_SELECTOR, "#menu-item-31832")
        self.talabalar_assotsiatsiyasi = (By.CSS_SELECTOR, "#menu-item-31833 > a")
        self.kutubxona = (By.CSS_SELECTOR, "#menu-item-31836 > a")
        self.go_to_photos = (By.CSS_SELECTOR, "#col-778809844 > div > p:nth-child(5)")
        self.kutubxona_photos = (By.CSS_SELECTOR, "#col-778809844 > div > div.row.large-columns-2.medium-columns-.small-columns-.row-xsmall > div:nth-child(1) > div > a > div > div.box-image.image-glow")
        self.btn_right = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-auto-cursor.mfp-ready > div > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close")
        self.kutubxona_photos_exit = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-auto-cursor.mfp-ready > button")
        self.oquv_jadvali = (By.CSS_SELECTOR, "#menu-item-31838 > a")
        self.academic_calendar_pdf = (By.CSS_SELECTOR, "#col-2072968619 > div > ul > li:nth-child(1) > a")

    def click_talabalar(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.talabalar))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_talabalar_assotsiatsiyasi(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.talabalar_assotsiatsiyasi)).click()

    def click_kutubxona(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.kutubxona)).click()

    def click_go_to_photos(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.go_to_photos))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_kutubxona_photos(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.kutubxona_photos))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_btn_right(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_right)).click()

    def click_kutubxona_photos_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.kutubxona_photos_exit)).click()

    def click_oquv_jadvali(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.oquv_jadvali)).click()

    def click_academic_calendar_pdf(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.academic_calendar_pdf))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_btn_back(self):
        # Вызываем встроенную команду истории браузера напрямую
        self.driver.execute_script("window.history.go(-1);")