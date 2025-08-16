from entities.InstagramSelectors import InstagramSelectors


class OpenFollowing:
    def __init__(self, marionette, username = None):
        self.marionette = marionette
        self.username = username

    def execute(self):
        if self.username is not None and self.username != "":
            self.marionette.navigate(url = InstagramSelectors.instagram_home_url + self.username)
        else:
            self.marionette.navigate(url = InstagramSelectors.instagram_home_url)
            self.marionette.click(css_selector = InstagramSelectors.profile_button, wait = True)
        self.marionette.click(css_selector = InstagramSelectors.following_link, wait = True)
        self.marionette.click(css_selector = InstagramSelectors.scrollable_div, wait = True)
