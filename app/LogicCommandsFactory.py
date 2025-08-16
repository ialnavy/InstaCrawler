from app.logic.GetUsersNotFollowingBack import GetUsersNotFollowingBack
from app.logic.MacroExtractFollowers import MacroExtractFollowers
from app.logic.MacroExtractFollowing import MacroExtractFollowing
from app.logic.RefineUsers import RefineUsers


class LogicCommandsFactory:

    def for_refine_users(self, marionette, users_as_dom_elements, refined_users = None):
        return RefineUsers(marionette, users_as_dom_elements, refined_users)

    def for_get_users_not_following_back(self, followers, following, not_following_back, username = None):
        return GetUsersNotFollowingBack(followers, following, not_following_back, username)

    def for_macro_extract_followers(self, factory_hub, marionette, username = None, users = None):
        return MacroExtractFollowers(factory_hub, marionette, username, users)

    def for_macro_extract_following(self, factory_hub, marionette, username = None, users = None):
        return MacroExtractFollowing(factory_hub, marionette, username, users)
