class GetUsersNotFollowingBack:
    def __init__(self, followers = [], following = [], not_following_back = [], username = None):
        self.followers = followers
        self.following = following
        self.not_following_back = not_following_back
        self.username = username
        self.not_following_back = []

    def __print_result(self):
        print(fr"""
[InstaCrawler] Result is ready!
    
{self.username} has {str(len(self.followers))} followers
{self.username} is following {str(len(self.following))} other users
""")
        print("Users not following back:")
        for user in self.not_following_back:
            print("- " + str(user))

    def execute(self):
        not_following_back = [\
            user_followed for user_followed in self.following\
                if user_followed.user_id not in\
                    {user_follower.user_id for user_follower in self.followers}]
        
        if self.not_following_back is None:
            self.not_following_back = []
        self.not_following_back[:] = not_following_back
        
        self.__print_result()

        return self.not_following_back