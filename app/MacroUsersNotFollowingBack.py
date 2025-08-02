from app.commands.CommandFactory import CommandFactory
from entities.InstagramSelectors import InstagramSelectors


class MacroUsersNotFollowingBack:

    def __init__(self):
        self.followers = []
        self.following = []
        self.not_following_back = []

        self.marionette = CommandFactory.for_create_marionette().execute()
        # The order of commands is important here, as they are individually
        # accessed later in the execute method.
        self.commands = [\
            CommandFactory.for_verify_login(marionette = self.marionette,\
                                            is_manual_verification = False),\
            CommandFactory.for_scrap_users(marionette = self.marionette,\
                                         users_container_selector =\
                                            InstagramSelectors.followers_link),\
            CommandFactory.for_scrap_users(marionette = self.marionette,\
                                         users_container_selector =\
                                            InstagramSelectors.following_link),\
            CommandFactory.for_destroy_marionette(marionette = self.marionette)]
        

    def __print_result(self):
        print(f"""
        [InstaCrawler] Result is ready!
            
        User has {str(len(self.followers))} followers
        User is following {str(len(self.following))} other users
        """)
        print("Users not following back:")
        for user in self.not_following_back:
            print("- " + str(user))


    def execute(self):
        for command in self.commands:
            command.execute()
        
        # These are accesses to individual commands in the
        # command stack. This is not the best practice,
        # but it is done here for simplicity.
        self.followers = self.commands[1].users
        self.following = self.commands[2].users

        self.not_following_back = [\
            item for item in self.following\
                if item.user_id not in\
                    {item.user_id for item in self.followers}]
        
        self.__print_result()
