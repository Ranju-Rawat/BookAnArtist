from selenium.webdriver.common.by import By


class designPage:
    def __init__(self, driver):
        self.driver = driver

    page_title = (By.XPATH, "//p[text()='Design']")
    back_btn = (By.XPATH, "//span[text()='Back']")
    design_process = (By.XPATH, "//span[text()='No idea']")
    job_description = (By.ID, "job_description")
    attach_file = (By.XPATH, "//button[@title='Attach file']")
    continue_btn = (By.XPATH, "//span[text()='Continue']")
    design_process_err_msg = (By.ID, "design_process_status_help")
    job_desc_err_msg = (By.ID, "job_description_help")
    attached_file = (By.CLASS_NAME, "s3-img-editor-file-icon-name")
