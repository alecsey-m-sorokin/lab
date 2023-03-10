from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def open_site(self, url: str) -> None:
        """ Открытие страницы по url """
        self.driver.get(url)

    def get(self, url):
        return self.driver.get(url)

    def close(self):
        return self.driver.close()

    def quit(self):
        return self.driver.quit()

    def find_element_presence(self, locator, delay=10):
        # Finds one presence_of_element by locator
        return WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find presence_of_element with locator {locator}.")

    def input_text(self, locator, text) -> None:
        """ Ввод значений в поля """
        self.find_element_presence(locator, delay=10).send_keys(text)
