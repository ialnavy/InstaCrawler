from bs4 import BeautifulSoup
from entities.InstagramSelectors import InstagramSelectors


class VerifyLogin:
    """Verify Instagram login status."""
    
    def __init__(self, marionette, is_manual_verification=False):
        self.marionette = marionette
        self.is_manual_verification = is_manual_verification

    def execute(self):
        print(r"""
[InstaCrawler] Verifying Instagram login status...
""")
        self.marionette.navigate(url = InstagramSelectors.instagram_home_url)

        dom_content = BeautifulSoup(self.marionette.get_html_content(), 'html.parser')
        
        is_input_username_found = dom_content.select_one(InstagramSelectors.input_username) is not None
        is_register_button_found = dom_content.select_one(InstagramSelectors.register_button) is not None

        is_logged_in = not is_input_username_found and not is_register_button_found

        if not is_logged_in or self.is_manual_verification:
            print(r"""
        [InstaCrawler] You have not yet logged into Instagram.
        [InstaCrawler] Please log in to your account and then run the script again.
        """)
            self.marionette.navigate_and_wait_forever(url = InstagramSelectors.instagram_home_url)
