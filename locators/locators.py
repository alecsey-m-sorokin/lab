from selenium.webdriver.common.by import By


class ToolsQaLocators:
    full_name = (By.XPATH, '//*[@id="userName"]')
    user_email = (By.XPATH, '//*[@id="userEmail"]')
    current_address = (By.XPATH, '//*[@id="currentAddress"]')
    permanent_address = (By.XPATH, '//*[@id="permanentAddress"]')
    submit_button = (By.XPATH, '//*[@id="submit"]')
    output_results = (By.XPATH, '//*[@id="output"]/div')
