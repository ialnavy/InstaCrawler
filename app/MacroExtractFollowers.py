class MacroExtractFollowers:
    def __init__(self, command_factory, marionette, username = None, users = None):
        self.command_factory = command_factory
        self.marionette = marionette
        self.username = username
        self.users = users

        self.refined_users = []
        self.users_as_dom_elements = []

        # The order of the command matters!!!
        self.commands = [\
            self.command_factory.for_open_followers(\
                marionette = self.marionette,\
                username = self.username),\
            
            self.command_factory.for_scrap_users(\
                marionette = self.marionette,\
                users_as_dom_elements = self.users_as_dom_elements),\
                
            self.command_factory.for_refine_users(\
                marionette = self.marionette,\
                users_as_dom_elements = self.users_as_dom_elements,\
                refined_users = self.refined_users)]


    def execute(self):
        for command in self.commands:
            command.execute()

        if self.users is None:
            self.users = []
        self.users[:] = self.refined_users
        
        return self.users
