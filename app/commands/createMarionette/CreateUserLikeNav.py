from marionette.UserLikeMsEdgeNav import UserLikeMsEdgeNav


class CreateUserLikeNav:
    """Class to create a UserLikeNav instance for Marionette navigation."""

    def __init__(self):
        self.marionette = None


    def execute(self):
        print(r"""
        [InstaCrawler] Starting Marionette browser session...
        """)
        self.marionette = UserLikeMsEdgeNav()
        return self.marionette
