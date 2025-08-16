from bs4 import BeautifulSoup

from entities.InstagramSelectors import InstagramSelectors


class ObtainUserProfile:
    def __init__(self, marionette, pojo):
        self.marionette = marionette
        self.username = None
        self.pojo = pojo

    def execute(self):
        print(r"""
[InstaCrawler] Retrieving logged username...
""")
        self.marionette.navigate(url = InstagramSelectors.instagram_home_url)
        self.marionette.click(css_selector = InstagramSelectors.profile_button, wait = True)

        username = None
        dom_content = BeautifulSoup(self.marionette.get_html_content(), 'html.parser')
        user_span = dom_content.select_one(InstagramSelectors.logged_user_id)
        if user_span is not None:
            username = str(user_span.text).strip()

        self.username = username
        self.pojo.set_username(self.username)

        print(fr"""
[InstaCrawler] Your username has been retrieved: '{self.username}'.
""")
        return self.username
