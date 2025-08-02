import os
import time

from entities.InstagramSelectors import InstagramSelectors


class ScrapUsersDom:

    def do_scrap_users_dom(self, marionette):
        for _ in range(int(float(os.getenv("TIMES_TO_SCROLL_DOWN_USER_CONTAINER")))):
            marionette.scroll_down(css_selector = InstagramSelectors.scrollable_div)
            time.sleep(float(os.getenv("SECONDS_TO_WAIT_AFTER_SCROLL")))
        time.sleep(float(os.getenv("SECONDS_TO_WAIT_FOR_USERS_CONTAINER_TO_LOAD")))
