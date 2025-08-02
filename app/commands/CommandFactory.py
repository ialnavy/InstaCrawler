from app.commands.createMarionette.CreateUserLikeNav import CreateUserLikeNav
from app.commands.destroyMarionette.DestroyMarionette import DestroyMarionette
from app.commands.scrapUsers.ScrapUsersFromHtml import ScrapUsersFromHtml
from app.commands.verifyLogin.VerifyLogin import VerifyLogin


class CommandFactory:
    """A factory class to create command instances."""


    @staticmethod
    def for_create_marionette():
        return CreateUserLikeNav()

    
    @staticmethod
    def for_verify_login(marionette, is_manual_verification):
        return VerifyLogin(marionette, is_manual_verification)
    

    @staticmethod
    def for_scrap_users(marionette, users_container_selector):
        return ScrapUsersFromHtml(marionette, users_container_selector)
    
    @staticmethod
    def for_destroy_marionette(marionette):
        return DestroyMarionette(marionette)
