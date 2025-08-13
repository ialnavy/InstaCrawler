from marionette.UserLikeMsEdgeNav import UserLikeMsEdgeNav


class CreateMarionette:
    """Class to create a UserLikeNav instance for Marionette navigation."""

    def __init__(self):
        self.marionette = None


    def execute(self):
        self.marionette = UserLikeMsEdgeNav()
        return self.marionette
