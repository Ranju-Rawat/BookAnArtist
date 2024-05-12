import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def pre_setup(request):
    browserName = request.config.getoption("browser_name").lower()
    if browserName == "chrome":
        driver_path = Service("C:\\Users\\rawat\\PycharmProjects\\BookAnArtist\\Drivers\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=driver_path)
        #driver.get("https://hireanartist.com.au/post-a-job")
        driver.get("https://hireanartist.com.au/graffiti-artists-melbourne")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        request.cls.driver = driver
        request.cls.wait = wait
        yield driver
        time.sleep(5)
        driver.quit()
    else:
        raise ValueError("Unsupported browser specified")
