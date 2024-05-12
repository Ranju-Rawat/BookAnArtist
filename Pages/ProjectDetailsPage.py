from selenium.webdriver.common.by import By


class project_details:
    def __init__(self, driver):
        self.driver = driver

    cookies_pop_up = (By.XPATH, "//div[@class='react-cookie-banner']")
    accept_cookies = (By.CLASS_NAME, "button-close")
    project_nm = (By.ID, "project_name")
    art_typ = (By.XPATH, "//span[text()='Portrait Art']")
    art_size_btn = (By.CLASS_NAME, "ant-select-selection-search")
    art_size = (By.XPATH, "//div[@title='A3']")
    proj_location = (By.XPATH, "//input[@placeholder='Search your location...']")
    suggestions = (By.XPATH, "//span[text()='Cambridge, UK']")
    continue_btn = (By.XPATH, "//span[text()='Continue']")
    project_nm_err_msg = (By.ID, "project_name_help")
    mural_loc_err_msg = (By.ID, "mural_on_help")
    project_loc_err_msg = (By.ID, "google_address_help")
    property_type_err_msg = (By.ID, "property_type_help")
    page_title = (By.XPATH, "//p[@class='h5-heading mb-0']")
    artist_names = (By.CSS_SELECTOR, "div[class='custom-flex-column custom-flex-align-start w-100']")
    prices = (By.XPATH, "//p[@class='p-s-txt font-style-uppercase small-txt-spacing txt-semiBold mb-0']")


