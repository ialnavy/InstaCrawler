class InstagramUser:
    """An Instagram user"""

    def __init__(self, user_id, full_name):
        self.user_id = user_id
        self.full_name = full_name

    def __str__(self):
        output = "" + self.full_name
        output += " (" + self.user_id + ")"
        return output
