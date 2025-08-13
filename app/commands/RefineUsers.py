import re

from entities.InstagramSelectors import InstagramSelectors
from entities.InstagramUser import InstagramUser


class RefineUsers:
    def __init__(self, marionette, users_as_dom_elements, refined_users = None):
        self.marionette = marionette
        self.users_as_dom_elements = users_as_dom_elements
        self.refined_users = refined_users

    def execute(self):
        refined_users = []
        for child in self.users_as_dom_elements:
            if child != '\n':
                userIdDom = child.select_one(InstagramSelectors.user_id_1)
                if userIdDom is None:
                    userIdDom = child.select_one(InstagramSelectors.user_id_2)
                userId = userIdDom.text

                userFullNameDom = child.select_one(InstagramSelectors.user_full_name)
                userFullName = userFullNameDom.text

                refined_users.append(InstagramUser(
                    user_id = re.sub(r'\s+', ' ', userId),
                    full_name = re.sub(r'\s+', ' ', userFullName)
                ))
        
        if self.refined_users is None:
            self.refined_users = []
        self.refined_users[:] = refined_users

        return self.refined_users
