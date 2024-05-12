import pytest
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("pre_setup")
class BaseClass:
    wait = None

    def element_to_be_clickable(self, element):
        return self.wait.until(expected_conditions.element_to_be_clickable(element))

    def get_multiple_elements(self, elements):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(elements))

    def check_visibility_of_element(self, element):
        return self.wait.until(expected_conditions.visibility_of_element_located(element))
