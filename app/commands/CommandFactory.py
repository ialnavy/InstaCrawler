from app.MacroManualLogin import MacroManualLogin
from app.MacroUsersNotFollowingBack import MacroUsersNotFollowingBack

from app.commands.createMarionette.CreateUserLikeNav import CreateUserLikeNav
from app.commands.destroyMarionette.DestroyMarionette import DestroyMarionette
from app.commands.scrapUsers.ScrapUsersFromHtml import ScrapUsersFromHtml
from app.commands.verifyLogin.VerifyLogin import VerifyLogin


class CommandFactory:
    """A factory class to create command instances."""


    # Aspect commands.
    # These atomic commands can be used across every part of the application.

    def for_create_marionette(self):
        return CreateUserLikeNav()

    def for_destroy_marionette(self, marionette):
        return DestroyMarionette(marionette)


    # Macro commands.
    # These commands are intended to be a set of atomic commands.

    def for_macro_manual_login(self, command_factory, marionette):
        return MacroManualLogin(command_factory, marionette)

    def for_macro_users_not_following_back(self, command_factory, marionette):
        return MacroUsersNotFollowingBack(command_factory, marionette)


    # Atomic commands.
    # These commands are individual tasks, which would be used by macros.

    def for_verify_login(self, marionette, is_manual_verification):
        return VerifyLogin(marionette, is_manual_verification)

    def for_scrap_users(self, marionette, users_container_selector, collection_name):
        return ScrapUsersFromHtml(marionette, users_container_selector, collection_name)
