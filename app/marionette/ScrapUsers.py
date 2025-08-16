import os
import time
from bs4 import BeautifulSoup

from entities.InstagramSelectors import InstagramSelectors


class ScrapUsers:
    def __init__(self, marionette, users_as_dom_elements = None):
        self.marionette = marionette
        self.users_as_dom_elements = users_as_dom_elements

    def _get_users_as_dom_elements(self):
        users = []
        dom_content = BeautifulSoup(self.marionette.get_html_content(), 'html.parser')
        container_of_users = dom_content.select_one(InstagramSelectors.container_of_users)
        if container_of_users is not None:
            users = list(container_of_users.children)
        return users

    def execute(self):
        previous_users_count = -1
        i_users_count = 0

        users_as_dom_elements = []
        while i_users_count != previous_users_count:
            previous_users_count = i_users_count
            users_as_dom_elements = self._get_users_as_dom_elements()
            
            for _ in range(int(float(os.getenv("TIMES_TO_SCROLL_DOWN_USER_CONTAINER")))):
                self.marionette.scroll_down(css_selector = InstagramSelectors.scrollable_div)
                time.sleep(float(os.getenv("SECONDS_TO_WAIT_AFTER_SCROLL")))
            time.sleep(float(os.getenv("SECONDS_TO_WAIT_FOR_USERS_CONTAINER_TO_LOAD")))

            i_users_count = len(users_as_dom_elements)

        if self.users_as_dom_elements is None:
            self.users_as_dom_elements = []
        self.users_as_dom_elements[:] = users_as_dom_elements

        return self.users_as_dom_elements
