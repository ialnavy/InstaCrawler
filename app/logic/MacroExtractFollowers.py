class MacroExtractFollowers:
    def __init__(self, factory_hub, marionette, pojo, users = None):
        self.factory_hub = factory_hub
        self.marionette = marionette
        self.pojo = pojo
        self.users = users

        self.refined_users = []
        self.users_as_dom_elements = []

        # The order of the command matters!!!
        self.commands = [\
            self.factory_hub.for_marionette_commands()\
                .for_open_followers(\
                    marionette = self.marionette,\
                    username = self.pojo.username),\
            
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
[InstaCrawler] Retrieving list of users who follow you.
""")
        for command in self.commands:
            command.execute()

        if self.users is None:
            self.users = []
        self.users[:] = self.refined_users
        
        return self.users
