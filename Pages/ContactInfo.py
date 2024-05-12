from selenium.webdriver.common.by import By


class contactInfo():

    def __init__(self, driver):
        self.driver = driver

    info_page_title = (By.XPATH, "//p[@class='h5-heading mb-0']")
    personal_interest_err_msg = (By.ID, "user_as_help")
    mobile_help_err_msg = (By.ID, "mobile_help")
    first_nm_err_msg = (By.ID, "first_name_help")
    last_nm_err_msg = (By.ID, "last_name_help")
    email_err_msg = (By.ID, "email_help")
    password_err_msg = (By.ID, "password_help")
    terms_err_msg = (By.ID, "terms_privacy_help")
    captcha_err_msg = (By.ID, "recaptch_help")
    back_btn = (By.XPATH, "//span[text()='Back']")
    submit_btn = (By.XPATH, "//span[text()='Save & submit']")
    personal_interest = (By.XPATH, "(//label)[2]")
    country_phone = (By.CLASS_NAME, "PhoneInputCountry")
    mobile_phone = (By.CLASS_NAME, "PhoneInputInput")
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    email = (By.ID, "email")
    password = (By.ID, "password")
    terms_privacy = (By.XPATH, "//div[@class='ant-form-item-control-input']/div/label/span")

