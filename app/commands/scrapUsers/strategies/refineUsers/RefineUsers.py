import re
from entities.InstagramUser import InstagramUser
from entities.InstagramSelectors import InstagramSelectors


class RefineUsers:

    def do_refine_users(self, users_as_dom_elements):
        users = []
        for child in users_as_dom_elements:
            if child != '\n':
                userId = child.select_one(InstagramSelectors.user_id).text
                userFullName = child.select_one(InstagramSelectors.user_full_name).text
                users.append(InstagramUser(
                    user_id = re.sub(r'\s+', ' ', userId),
                    full_name = re.sub(r'\s+', ' ', userFullName)
                ))
        return users
