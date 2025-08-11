class MacroExtractFollowing:
    def __init__(self, command_factory, marionette, username = None):
        self.command_factory = command_factory
        self.marionette = marionette
        self.username = username
        self.users = []

    def execute(self):
        # Go to following list
        self.command_factory.for_open_following(self.marionette, self.username).execute()

        # Scrap users as HTML DOM elements
        users_as_dom_elements = self.command_factory.for_scrap_users(self.marionette).execute()

        # Refine the list of users into custom objects
        self.users = self.command_factory.for_refine_users(\
                        self.marionette, users_as_dom_elements)\
                            .execute()
        
        return self.users
