class ExtractFollowingOrder:

    def __init__(self, factory_hub, marionette):
        self.factory_hub = factory_hub
        self.marionette = marionette
        self.username = ""
        self.following = []

        self.commands = [\
            self.factory_hub.for_marionette_commands()\
                .for_obtain_user_profile(\
                    marionette = self.marionette,\
                    pojo = self),\

            self.factory_hub.for_logic_commands()\
                .for_macro_extract_following(\
                    factory_hub = self.factory_hub,\
                    marionette = self.marionette,\
                    pojo = self,\
                    users = self.following),\

            self.factory_hub.for_logic_commands()\
                .for_export_users(\
                    factory_hub = self.factory_hub,\
                    subdir = self.factory_hub.for_config()['paths']['export_following_subdir'],\
                    pojo = self,\
                    users = self.following),\

            self.factory_hub.for_marionette_commands()\
                .for_destroy_marionette(marionette = self.marionette)\
        ]

    def set_username(self, username):
        self.username = username

    def execute(self):
        for command in self.commands:
            command.execute()
