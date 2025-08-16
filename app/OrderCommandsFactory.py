from app.order.UsersNotFollowingBackOrder import UsersNotFollowingBackOrder


class OrderCommandsFactory:

    def for_users_not_following_back_order(self, factory_hub, marionette):
        return UsersNotFollowingBackOrder(factory_hub, marionette)
