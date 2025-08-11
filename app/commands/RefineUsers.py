import re

from entities.InstagramSelectors import InstagramSelectors
from entities.InstagramUser import InstagramUser


class RefineUsers:
    def __init__(self, marionette, users_as_dom_elements):
        self.marionette = marionette
        self.users_as_dom_elements = users_as_dom_elements
        self.users = []

    def execute(self):
        self.users = []
        for child in self.users_as_dom_elements:
            if child != '\n':
                userId = child.select_one(InstagramSelectors.user_id).text
                userFullName = child.select_one(InstagramSelectors.user_full_name).text
                self.users.append(InstagramUser(
                    user_id = re.sub(r'\s+', ' ', userId),
                    full_name = re.sub(r'\s+', ' ', userFullName)
                ))
        return self.users
