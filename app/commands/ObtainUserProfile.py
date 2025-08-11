from bs4 import BeautifulSoup

from entities.InstagramSelectors import InstagramSelectors


class ObtainUserProfile:
    def __init__(self, marionette):
        self.marionette = marionette

    def execute(self):
        self.marionette.navigate(url = InstagramSelectors.instagram_home_url)
        self.marionette.click(css_selector = InstagramSelectors.profile_button, wait = True)

        username = None
        dom_content = BeautifulSoup(self.marionette.get_html_content(), 'html.parser')
        user_span = dom_content.select_one(InstagramSelectors.logged_user_id)
        if user_span is not None:
            username = str(user_span.text).strip()
        return username
