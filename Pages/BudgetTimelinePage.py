from selenium.webdriver.common.by import By


class budgetTimeline:

    def __init__(self, driver):
        self.driver = driver

    page_title = (By.XPATH, "//p[@class='h5-heading mb-0']")
    back_btn = (By.XPATH, "//span[text()='Back']")
    continue_btn = (By.XPATH, "//span[text()='Continue']")
    budget_err_msg = (By.ID, "budget_help")
    artwork_dt_err_msg = (By.ID, "deadline_type_help")
    enter_budget = (By.ID, "budget")
    countries_dropdown = (By.ID, "currency")
    scroll_down = (By.ID, "currency_list")
    select_country = (By.CLASS_NAME, "ant-select-item-option-content")
    date_picker = (By.XPATH, "(//div[@class='ant-picker-input'])[1]")
    deadline_date = (By.XPATH, "(//tbody)[1]/tr/td")
    open_before_dt_calendar = (By.XPATH, "(//div[@class='ant-picker-input'])[2]")
    before_date = (By.XPATH, "(//tbody)[2]/tr/td")
