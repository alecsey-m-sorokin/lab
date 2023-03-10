import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver(request):
    driver = Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()
