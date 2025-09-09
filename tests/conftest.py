import time

import pytest
from selenium import webdriver
import tempfile
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(request):

    chrome_options = Options()
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")  

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")  # Optional: run without GUI

    driver = webdriver.Chrome(options=chrome_options)
    #driver.implicitly_wait(60)
    driver.get("https://accounts2.netgear.com/login?redirectUrl=https:%2F%2Finsight.netgear.com%2F&clientId=6dlf5ppqm5oic7hhtk68qrlc9j")
    time.sleep(3)
    request.cls.driver = driver
    yield
    driver.quit()







