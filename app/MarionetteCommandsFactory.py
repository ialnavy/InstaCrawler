from app.marionette.DestroyMarionette import DestroyMarionette
from app.marionette.ObtainUserProfile import ObtainUserProfile
from app.marionette.OpenFollowers import OpenFollowers
from app.marionette.OpenFollowing import OpenFollowing
from app.marionette.ScrapUsers import ScrapUsers
from app.marionette.VerifyLogin import VerifyLogin


class MarionetteCommandsFactory:

    def for_verify_login(self, marionette, is_manual_verification):
        return VerifyLogin(marionette, is_manual_verification)

    def for_obtain_user_profile(self, marionette, pojo):
        return ObtainUserProfile(marionette, pojo)
    
    def for_open_followers(self, marionette, username = None):
        return OpenFollowers(marionette, username)
    
    def for_open_following(self, marionette, username = None):
        return OpenFollowing(marionette, username)
    
    def for_scrap_users(self, marionette, users_as_dom_elements = None):
        return ScrapUsers(marionette, users_as_dom_elements)

    def for_destroy_marionette(self, marionette):
        return DestroyMarionette(marionette)
