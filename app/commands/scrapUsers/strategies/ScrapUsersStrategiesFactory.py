from app.commands.scrapUsers.strategies.listUsersDom.ListUsersDom import ListUsersDom
from app.commands.scrapUsers.strategies.refineUsers.RefineUsers import RefineUsers
from app.commands.scrapUsers.strategies.scrapUsersDom.ScrapUsersDom import ScrapUsersDom


class ScrapUsersStrategiesFactory:

    @staticmethod
    def for_list_users_dom():
        return ListUsersDom()
    
    @staticmethod
    def for_scrap_users_dom():
        return ScrapUsersDom()
    
    @staticmethod
    def for_refine_users():
        return RefineUsers()
