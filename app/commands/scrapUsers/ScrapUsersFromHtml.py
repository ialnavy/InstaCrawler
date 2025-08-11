from app.commands.scrapUsers.strategies.ScrapUsersStrategiesFactory import ScrapUsersStrategiesFactory
from entities.InstagramSelectors import InstagramSelectors


class ScrapUsersFromHtml:
    """A command to retrieve the users from HTML DOM container."""
    
    def __init__(self, marionette, users_container_selector, collection_name):
        self.marionette = marionette
        self.users_container_selector = users_container_selector
        self.collection_name = collection_name
        self.users = []


    def execute(self):
        print(r"""
[InstaCrawler] Retrieving users...
""")
        self.marionette.navigate(url = InstagramSelectors.instagram_home_url)
        self.marionette.click(css_selector = InstagramSelectors.profile_button, wait = True)
        self.marionette.click(css_selector = self.users_container_selector, wait = True)
        self.marionette.click(css_selector = InstagramSelectors.scrollable_div, wait = True)

        previous_users_count = -1
        i_users_count = 0
        users_as_dom_elements = []

        while i_users_count != previous_users_count:
            previous_users_count = i_users_count
            users_as_dom_elements = ScrapUsersStrategiesFactory.for_list_users_dom()\
                .do_list_users_dom(marionette = self.marionette)
            ScrapUsersStrategiesFactory.for_scrap_users_dom()\
                .do_scrap_users_dom(marionette = self.marionette)
            i_users_count = len(users_as_dom_elements)

        self.users = ScrapUsersStrategiesFactory.for_refine_users()\
                        .do_refine_users(users_as_dom_elements = users_as_dom_elements)
