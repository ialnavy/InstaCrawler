from app.MacroExtractFollowers import MacroExtractFollowers
from app.MacroExtractFollowing import MacroExtractFollowing

from app.commands.CreateMarionette import CreateMarionette
from app.commands.DestroyMarionette import DestroyMarionette
from app.commands.ExportUsersNotFollowingBack import ExportUsersNotFollowingBack
from app.commands.ObtainUserProfile import ObtainUserProfile
from app.commands.OpenFollowers import OpenFollowers
from app.commands.OpenFollowing import OpenFollowing
from app.commands.RefineUsers import RefineUsers
from app.commands.ScrapUsers import ScrapUsers
from app.commands.VerifyLogin import VerifyLogin


class CommandFactory:
    """A factory class to create command instances."""


    # Steps manipulating the marionette.
    # ----------------------------------

    def for_create_marionette(self):
        return CreateMarionette()

    def for_verify_login(self, marionette, is_manual_verification):
        return VerifyLogin(marionette, is_manual_verification)

    def for_obtain_user_profile(self, marionette):
        return ObtainUserProfile(marionette)
    
    def for_open_followers(self, marionette, username = None):
        return OpenFollowers(marionette, username)
    
    def for_open_following(self, marionette, username = None):
        return OpenFollowing(marionette, username)
    
    def for_scrap_users(self, marionette):
        return ScrapUsers(marionette)

    def for_destroy_marionette(self, marionette):
        return DestroyMarionette(marionette)
    

    # Tasks independent of the marionette.
    # ------------------------------------

    def for_refine_users(self, marionette, users_as_dom_elements):
        return RefineUsers(marionette, users_as_dom_elements)
    
    def for_export_users_not_following_back(self, followers, following, username = None):
        return ExportUsersNotFollowingBack(followers, following, username)


    # Macro commands.
    # ---------------

    def for_macro_extract_followers(self, command_factory, marionette, username = None):
        return MacroExtractFollowers(command_factory, marionette, username)
    
    def for_macro_extract_following(self, command_factory, marionette, username = None):
        return MacroExtractFollowing(command_factory, marionette, username)
