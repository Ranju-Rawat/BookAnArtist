# import subprocess
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from Pages.BudgetTimelinePage import budgetTimeline
# from Pages.ContactInfo import contactInfo
# from Pages.DesignPage import designPage
# from Pages.ProjectDetailsPage import project_details
# from Utilities.BaseClass import BaseClass
#
#
# class TestProjectDetails(BaseClass):
#     driver = None
#
#     def test_browser_url(self):
#         """Verify that the correct title is displayed on the website"""
#         print(self.driver.title)
#         website_title = self.driver.title
#         assert "Book An Artist" in website_title, "Expected title not found in website title"
#
#     def _handle_cookies_popup(self, page):
#         """Handle cookies popup if present"""
#         cookies_popup = self.check_visibility_of_element(page.cookies_pop_up)
#         if cookies_popup.is_displayed():
#             accept_cookies = self.element_to_be_clickable(page.accept_cookies)
#             accept_cookies.click()
#
#     def test_empty_project_details_form(self):
#         """Verify error messages are displayed for empty project details form"""
#         project_details_page = project_details(self.driver)
#         self._handle_cookies_popup(project_details_page)
#         continue_btn = self.element_to_be_clickable(project_details_page.continue_btn)
#         continue_btn.click()
#         # Verifying error messages
#         proj_nm_err_msg = self.check_visibility_of_element(project_details_page.project_nm_err_msg).text
#         mural_loc_err_msg = self.check_visibility_of_element(project_details_page.mural_loc_err_msg).text
#         project_loc_err_msg = self.check_visibility_of_element(project_details_page.project_loc_err_msg).text
#         prop_type_err_msg = self.check_visibility_of_element(project_details_page.property_type_err_msg).text
#         assert proj_nm_err_msg == "Please input a project name!", "Incorrect project name error message"
#         assert mural_loc_err_msg == "Please select option!", "Incorrect mural location error message"
#         assert project_loc_err_msg == "Please input your address", "Incorrect project location error message"
#         assert prop_type_err_msg == "Please select a property type!", "Incorrect property type error message"
#
#     def test_valid_project_details_form(self):
#         """Fill and submit valid project details"""
#         project_details_page = project_details(self.driver)
#         design_page = designPage(self.driver)
#         enter_project_name = self.element_to_be_clickable(project_details_page.project_nm)
#         enter_project_name.send_keys("Public Window Mural – Canada")
#         # Validate project name length
#         assert len(enter_project_name.get_attribute("value")) >= 10, "Project name should be at least 10 characters long"
#         select_art_type = self.element_to_be_clickable(project_details_page.art_typ)
#         select_art_type.click()
#         click_art_dropdown = self.element_to_be_clickable(project_details_page.art_size_btn)
#         click_art_dropdown.click()
#         select_art_size = self.element_to_be_clickable(project_details_page.art_size)
#         select_art_size.click()
#         enter_project_location = self.element_to_be_clickable(project_details_page.proj_location)
#         enter_project_location.send_keys("Cambridge")
#         location = self.check_visibility_of_element(project_details_page.suggestions)
#         location.click()
#         click_continue_btn = self.element_to_be_clickable(project_details_page.continue_btn)
#         click_continue_btn.click()
#         design_page_title = self.check_visibility_of_element(design_page.page_title).text
#         # Verify navigation to design page
#         assert design_page_title == "Design", "Expected title not found in website title"
#
#     def test_back_navigation_from_design_form(self):
#         project_details_page = project_details(self.driver)
#         design_page = designPage(self.driver)
#         back_btn = self.element_to_be_clickable(design_page.back_btn)
#         back_btn.click()
#         project_det_page_title = self.check_visibility_of_element(project_details_page.page_title).text
#         assert project_det_page_title == "Let's start with the basics", ("Incorrect page title error "
#                                                                          "message")
#         click_continue_btn = self.element_to_be_clickable(project_details_page.continue_btn)
#         click_continue_btn.click()
#
#     def test_empty_design_form(self):
#         design_page = designPage(self.driver)
#         click_continue_btn = self.element_to_be_clickable(design_page.continue_btn)
#         click_continue_btn.click()
#         design_process_err_msg = self.check_visibility_of_element(design_page.design_process_err_msg).text
#         job_desc_err_msg = self.check_visibility_of_element(design_page.job_desc_err_msg).text
#         assert design_process_err_msg == "Please select a design process!", "Incorrect design process error message"
#         assert job_desc_err_msg == "Please input your message!", "Incorrect job description error message"
#
#     def _handle_upload_file(self, design_page):
#         autoit_script = "C:\\Users\\rawat\\Downloads\\fileUpload.exe"
#         try:
#             # Execute the AutoIt script using subprocess
#             process = subprocess.Popen(autoit_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             stdout, stderr = process.communicate()
#
#             # Print output and error
#             print("Output:", stdout.decode())
#             print("Error:", stderr.decode())
#             attached_file = self.check_visibility_of_element(design_page.attached_file)
#             if attached_file.is_displayed():
#                 attached_file_text = attached_file.text
#                 assert attached_file_text == "test - Sheet1.pdf", "Incorrect file"
#             else:
#                 print("File does not uploaded")
#         except Exception as e:
#             print("An error occurred while executing the subprocess:", e)
#             screenshot = "C:\\Users\\rawat\\PycharmProjects\\BookAnArtist\\Reports\\screenshot_name.png"
#             self.driver.get_screenshot_as_file(screenshot)
#
#     def test_valid_design_form(self):
#         design_page = designPage(self.driver)
#         design_process = self.element_to_be_clickable(design_page.design_process)
#         design_process.click()
#         job_description = self.element_to_be_clickable(design_page.job_description)
#         job_description.send_keys("We are seeking an experienced mural artist to create a captivating mural for a "
#                                   "public window space measuring 5ft x 5ft in Canada")
#         file_input = self.element_to_be_clickable(design_page.attach_file)
#         file_input.click()
#         time.sleep(3)
#         self._handle_upload_file(design_page)
#         continue_btn = self.element_to_be_clickable(design_page.continue_btn)
#         continue_btn.click()
#
#     def test_back_navigation_from_budgettimeline_form(self):
#         budget_timeline_page = budgetTimeline(self.driver)
#         design_page = designPage(self.driver)
#         back_btn = self.element_to_be_clickable(budget_timeline_page.back_btn)
#         back_btn.click()
#         design_page_title = self.check_visibility_of_element(design_page.page_title).text
#         assert design_page_title == "Design", "Incorrect page title error message"
#         click_continue_btn = self.element_to_be_clickable(design_page.continue_btn)
#         click_continue_btn.click()
#
#     def test_empty_budget_timeline_form(self):
#         budget_timeline_page = budgetTimeline(self.driver)
#         click_continue_btn = self.element_to_be_clickable(budget_timeline_page.continue_btn)
#         click_continue_btn.click()
#         budget_err_msg = self.check_visibility_of_element(budget_timeline_page.budget_err_msg).text
#         artwork_deadline_err_msg = self.check_visibility_of_element(budget_timeline_page.artwork_dt_err_msg).text
#         assert budget_err_msg == "Please provide a budget for your project!", "Incorrect budget error message"
#         assert artwork_deadline_err_msg == "Please select deadline!", "Incorrect artwork deadline error message"
#
#     def test_valid_budget_design_form(self):
#         contact_info_page = contactInfo(self.driver)
#         budget_timeline_page = budgetTimeline(self.driver)
#         enter_budget = self.element_to_be_clickable(budget_timeline_page.enter_budget)
#         enter_budget.send_keys("100.50")
#         countries_dropdown = self.element_to_be_clickable(budget_timeline_page.countries_dropdown)
#         countries_dropdown.send_keys("CAD")
#         select_country = self.element_to_be_clickable(budget_timeline_page.select_country)
#         select_country.click()
#         open_calendar = self.element_to_be_clickable(budget_timeline_page.date_picker)
#         open_calendar.click()
#         dates = self.get_multiple_elements(budget_timeline_page.deadline_date)
#         for date in dates:
#             title = date.get_attribute("title")
#             class_names = date.get_attribute("class")
#             if title == "2024-04-30" and "ant-picker-cell-disabled" not in class_names:
#                 date.click()
#                 break
#             elif title == "2024-05-11" and "ant-picker-cell-disabled" not in class_names:
#                 date.click()
#                 break
#
#         open_before_date_calendar = self.element_to_be_clickable(budget_timeline_page.open_before_dt_calendar)
#         open_before_date_calendar.click()
#         before_dates = self.get_multiple_elements(budget_timeline_page.before_date)
#         for before_date in before_dates:
#             title = before_date.get_attribute("title")
#             before_dt_class_names = before_date.get_attribute("class")
#             if title == "2024-05-20" and "ant-picker-cell-disabled" not in before_dt_class_names:
#                 before_date.click()
#                 break
#
#         click_continue_btn = self.element_to_be_clickable(budget_timeline_page.continue_btn)
#         click_continue_btn.click()
#         info_page_title = self.check_visibility_of_element(contact_info_page.info_page_title).text
#         assert info_page_title == "Contact Information", "Incorrect information page title error message"
#
#     def test_back_navigation_from_contactInfo_form(self):
#         contact_info_page = contactInfo(self.driver)
#         budget_timeline_page = budgetTimeline(self.driver)
#         back_btn = self.element_to_be_clickable(contact_info_page.back_btn)
#         back_btn.click()
#         budget_page_title = self.check_visibility_of_element(budget_timeline_page.page_title).text
#         assert budget_page_title == "Budget & Timeline", "Incorrect budget error message"
#         click_continue_btn = self.element_to_be_clickable(budget_timeline_page.continue_btn)
#         click_continue_btn.click()
#
#     def test_empty_contact_info_form(self):
#         contact_info_page = contactInfo(self.driver)
#         click_continue_btn = self.element_to_be_clickable(contact_info_page.submit_btn)
#         click_continue_btn.click()
#         personal_interest_err_msg = self.check_visibility_of_element(contact_info_page.personal_interest_err_msg).text
#         mobile_err_msg = self.check_visibility_of_element(contact_info_page.mobile_help_err_msg).text
#         first_name_err_msg = self.check_visibility_of_element(contact_info_page.first_nm_err_msg).text
#         last_name_err_msg = self.check_visibility_of_element(contact_info_page.last_nm_err_msg).text
#         email_err_msg = self.check_visibility_of_element(contact_info_page.email_err_msg).text
#         password_err_msg = self.check_visibility_of_element(contact_info_page.password_err_msg).text
#         terms_err_msg = self.check_visibility_of_element(contact_info_page.terms_err_msg).text
#         captcha_err_msg = self.check_visibility_of_element(contact_info_page.captcha_err_msg).text
#
#         assert personal_interest_err_msg == "Please select!", "Incorrect personal interest error message"
#         assert mobile_err_msg == "Please input your mobile number!", "Incorrect mobile error message"
#         assert first_name_err_msg == "Please input First Name!", "Incorrect first name error message"
#         assert last_name_err_msg == "Please input Last Name!", "Incorrect last name error message"
#         assert email_err_msg == "Please enter a valid email address!", "Incorrect email error message"
#         assert password_err_msg == "Please input your password!", "Incorrect password error message"
#         assert terms_err_msg == "Should accept agreement", "Incorrect terms error message"
#         assert captcha_err_msg == "Please check the checkbox for verification!", "Incorrect captcha error message"
#
#     def test_valid_contact_info_form(self):
#         contact_info_page = contactInfo(self.driver)
#         personal_interest = self.element_to_be_clickable(contact_info_page.personal_interest)
#         personal_interest.click()
#         click_on_code = self.element_to_be_clickable(contact_info_page.country_phone)
#         click_on_code.click()
#         select_dropdown = click_on_code.find_element(By.CLASS_NAME, "PhoneInputCountrySelect")
#         select = Select(select_dropdown)
#         select.select_by_visible_text("United Kingdom")
#         enter_mobile = self.element_to_be_clickable(contact_info_page.mobile_phone)
#         enter_mobile.send_keys("7070707070")
#         enter_first_name = self.element_to_be_clickable(contact_info_page.first_name)
#         enter_first_name.send_keys("Ranju")
#         enter_last_name = self.element_to_be_clickable(contact_info_page.last_name)
#         enter_last_name.send_keys("Rawat")
#         enter_email = self.element_to_be_clickable(contact_info_page.email)
#         enter_email.send_keys("ranju@gmail.com")
#         enter_password = self.element_to_be_clickable(contact_info_page.password)
#         enter_password.send_keys("ranju12345")
#         check_terms_privacy = self.element_to_be_clickable(contact_info_page.terms_privacy)
#         check_terms_privacy.click()
#         try:
#             # Manually complete CAPTCHA
#             time.sleep(25)
#             submit_form = self.element_to_be_clickable(contact_info_page.submit_btn)
#             submit_form.click()
#         except Exception as e:
#             print(f"Error occurred during form submission: {e}")
#             screenshot = "C:\\Users\\rawat\\PycharmProjects\\BookAnArtist\\Reports\\screenshot_name.png"
#             self.driver.get_screenshot_as_file(screenshot)
#
#
#
from Pages.ProjectDetailsPage import project_details
from Utilities.BaseClass import BaseClass


class TestProjectDetails(BaseClass):
    driver = None

    def test_user_details(self):
        proj_det_page = project_details(self.driver)
        artist_names = self.get_multiple_elements(proj_det_page.artist_names)

        for artist in artist_names:
            art_nm = artist.text.split()
            art_country = " ".join(art_nm[-2:])
            for each in art_nm:
                artist.text.remove(each)
            print("artist", art_country)

        prices = self.get_multiple_elements(proj_det_page.prices)

        for price in prices:
            print("prices text", price.text)

