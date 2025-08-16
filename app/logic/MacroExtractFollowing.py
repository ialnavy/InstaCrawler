class MacroExtractFollowing:
    def __init__(self, factory_hub, marionette, username = None, users = None):
        self.factory_hub = factory_hub
        self.marionette = marionette
        self.username = username
        self.users = users

        self.refined_users = []
        self.users_as_dom_elements = []

        # The order of the command matters!!!
        self.commands = [\
            self.factory_hub.for_marionette_commands()\
                .for_open_following(\
                    marionette = self.marionette,\
                    username = self.username),\
            
            self.factory_hub.for_marionette_commands()\
                .for_scrap_users(\
                    marionette = self.marionette,\
                    users_as_dom_elements = self.users_as_dom_elements),\
                
            self.factory_hub.for_logic_commands()\
                .for_refine_users(\
                    marionette = self.marionette,\
                    users_as_dom_elements = self.users_as_dom_elements,\
                    refined_users = self.refined_users)]


    def execute(self):
        print(r"""
[InstaCrawler] Retrieving list of users whom you are following.
""")
        for command in self.commands:
            command.execute()

        if self.users is None:
            self.users = []
        self.users[:] = self.refined_users
        
        return self.users
