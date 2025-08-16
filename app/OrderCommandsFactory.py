from app.order.ExtractFollowersOrder import ExtractFollowersOrder
from app.order.ExtractFollowingOrder import ExtractFollowingOrder
from app.order.UsersNotFollowingBackCompleteOrder import UsersNotFollowingBackCompleteOrder
from app.order.UsersNotFollowingBackOrder import UsersNotFollowingBackOrder


class OrderCommandsFactory:

    def for_extract_followers_order(self, factory_hub, marionette):
        return ExtractFollowersOrder(factory_hub, marionette)
    
    def for_extract_following_order(self, factory_hub, marionette):
        return ExtractFollowingOrder(factory_hub, marionette)

    def for_users_not_following_back_order(self, factory_hub):
        return UsersNotFollowingBackOrder(factory_hub)

    def for_users_not_following_back_complete_order(self, factory_hub, marionette):
        return UsersNotFollowingBackCompleteOrder(factory_hub, marionette)
