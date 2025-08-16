from app.logic.ExportUsers import ExportUsers
from app.logic.GetUsersNotFollowingBack import GetUsersNotFollowingBack
from app.logic.MacroExtractFollowers import MacroExtractFollowers
from app.logic.MacroExtractFollowing import MacroExtractFollowing
from app.logic.ReadUsers import ReadUsers
from app.logic.RefineUsers import RefineUsers


class LogicCommandsFactory:

    def for_export_users(self, factory_hub, subdir, pojo, users = []):
        return ExportUsers(factory_hub, subdir, pojo, users)
    
    def for_read_users(self, factory_hub, subdir, pojo, users = []):
        return ReadUsers(factory_hub, subdir, pojo, users)

    def for_refine_users(self, marionette, users_as_dom_elements, refined_users = None):
        return RefineUsers(marionette, users_as_dom_elements, refined_users)

    def for_get_users_not_following_back(self, pojo, followers, following, not_following_back):
        return GetUsersNotFollowingBack(pojo, followers, following, not_following_back)

    def for_macro_extract_followers(self, factory_hub, marionette, pojo, users = None):
        return MacroExtractFollowers(factory_hub, marionette, pojo, users)

    def for_macro_extract_following(self, factory_hub, marionette, pojo, users = None):
        return MacroExtractFollowing(factory_hub, marionette, pojo, users)
