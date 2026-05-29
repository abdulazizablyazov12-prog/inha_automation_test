import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver_chrome():
    options = Options()
    # Обязательные аргументы для стабильной работы Selenium внутри GitHub Actions
    options.add_argument("--headless=new")  # Запуск в фоновом режиме (стандарт для CI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Заменяет maximize_window()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()