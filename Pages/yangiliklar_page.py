from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class YangiliklarPage:
    def __init__(self, driver):
        self.driver = driver
        self.yangiliklar = (By.CSS_SELECTOR, "#menu-item-4622 > a")
        self.yangiliklar_card = (By.CSS_SELECTOR, "#content > div > div.large-9.col > div > div > div > div:nth-child(1) > div > a")
        self.img = (By.CSS_SELECTOR, "#post-41564 > div > div > div.row.large-columns-1.medium-columns-.small-columns-.slider.row-slider.slider-nav-reveal.is-draggable.flickity-enabled > div > div > div.gallery-col.col.is-selected > div > a > div > div.box-image > img")
        self.img_btn_right = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-auto-cursor.mfp-ready > div > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close")
        self.img_btn_exit = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-auto-cursor.mfp-ready > button")

    def click_yangiliklar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.yangiliklar)).click()

    def click_yangiliklar_card(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.yangiliklar_card))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_img(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.img))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_img_btn_right(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.img_btn_right)).click()

    def click_img_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.img_btn_exit)).click()
