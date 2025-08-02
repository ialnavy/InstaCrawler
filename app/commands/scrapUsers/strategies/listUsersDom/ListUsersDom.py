from bs4 import BeautifulSoup

from entities.InstagramSelectors import InstagramSelectors


class ListUsersDom:

    def do_list_users_dom(self, marionette):
        users = []
        dom_content = BeautifulSoup(marionette.get_html_content(), 'html.parser')
        container_of_users = dom_content.select_one(InstagramSelectors.container_of_users)
        if container_of_users is not None:
            users = list(container_of_users.children)
        return users
