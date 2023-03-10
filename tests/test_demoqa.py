import random
import time
from loguru import logger

from locators.locators import ToolsQaLocators
from pages.base_page import BasePage


class TestToolsQa:

    def test_01_fill_user_data(self, driver):

        full_name = random.choice([('Alecsey Ivanov'), ('Dmitry Petrov'), ('Oleg Smirnov')])
        user_email = random.choice([('test389@sample.com'), ('test318@sample.com'), ('test769@sample.com')])
        current_address = random.choice([('address Minsk 01'), ('address Minsk 02'), ('address Minsk 03')])
        permanent_address = random.choice([('address Mogilev 01'), ('address Mogilev 02'), ('address Mogilev 03')])
        logger.info(f'{full_name} / {user_email} / {current_address} / {permanent_address}')

        base_page = BasePage(driver)
        base_page.open_site(f'{"https://demoqa.com/text-box"}')
        time.sleep(1)

        base_page.find_element_presence(locator=ToolsQaLocators.full_name).click()
        base_page.input_text(ToolsQaLocators.full_name, text=full_name)

        base_page.find_element_presence(locator=ToolsQaLocators.user_email).click()
        base_page.input_text(ToolsQaLocators.user_email, text=user_email)

        base_page.find_element_presence(locator=ToolsQaLocators.current_address).click()
        base_page.input_text(ToolsQaLocators.current_address, text=current_address)

        base_page.find_element_presence(locator=ToolsQaLocators.permanent_address).click()
        base_page.input_text(ToolsQaLocators.permanent_address, text=permanent_address)

        base_page.find_element_presence(locator=ToolsQaLocators.submit_button).click()

        response_output = base_page.find_element_presence(locator=ToolsQaLocators.output_results).text
        logger.info(response_output)

        time.sleep(1)
        assert full_name in response_output, f'error, {full_name} is not found in response'
        assert user_email in response_output, f'error, {user_email} is not found in response'
        assert current_address in response_output, f'error, {current_address} is not found in response'
        assert permanent_address in response_output, f'error, {permanent_address} is not found in response'

