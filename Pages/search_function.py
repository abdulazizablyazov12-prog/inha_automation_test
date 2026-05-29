from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Search:
    def __init__(self, driver):
        self.driver = driver
        self.search_logo = (By.CSS_SELECTOR, "#wide-nav > div > div.flex-col.hide-for-medium.flex-right.flex-grow > ul > li.header-search.header-search-dropdown.has-icon.has-dropdown.menu-item-has-children > a > i")
        self.input_search = (By.CSS_SELECTOR, "#s")
        self.search_result = (By.CSS_SELECTOR, "#wide-nav > div > div.flex-col.hide-for-medium.flex-right.flex-grow > ul > li.header-search.header-search-dropdown.has-icon.has-dropdown.menu-item-has-children > ul > li > div > div > form > div.live-search-results.text-left.z-top > div > div:nth-child(2) > div")
        self.search_photo = (By.CSS_SELECTOR, "#post-41257 > div > div > div.row.large-columns-2.medium-columns-.small-columns-.slider.row-slider.slider-nav-simple.slider-nav-push.is-draggable.flickity-enabled > div > div > div:nth-child(1) > div > a > div > div.box-image > img")
        self.search_photo_btn_right = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-auto-cursor.mfp-ready > div > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close")
        self.search_photo_btn_exit = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-auto-cursor.mfp-ready > button")
        self.main_menu = (By.CSS_SELECTOR, "#breadcrumbs > span > span:nth-child(1) > a")

    def click_search_logo(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.search_logo))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def write_input_search(self, input_search):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.input_search)).send_keys(input_search)

    def click_search_result(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.search_result)).click()

    def click_search_photo(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.search_photo))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_search_photo_btn_right(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.search_photo_btn_right)).click()

    def click_search_photo_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.search_photo_btn_exit)).click()

    def click_btn_main_menu(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.main_menu))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()
