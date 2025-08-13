import sys

from dotenv import load_dotenv

from app.CommandFactory import CommandFactory
from entities.InstagramSelectors import InstagramSelectors


# Load environment variables from .env file
load_dotenv()

available_orders = [\
    "help",\
    "manual_login",\
    "not_following_back"]

def print_usage():
    print(f"Usage: python {sys.argv[0]} <{' | '.join(available_orders)}>")

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in available_orders:
        print("[InstaCrawler] Bad order detected.")
        print_usage()
        sys.exit(1)

    # Get the order from command line arguments
    # The "help" order would discard the rest of the code
    order = sys.argv[1]
    if order == "help":
        print("[InstaCrawler] See help below.")
        print_usage()
        sys.exit(0)

    # Initialise the command factory and marionette
    print(r"""
[InstaCrawler] Initialising command factory and marionette...
""")
    command_factory = CommandFactory()
    marionette = command_factory.for_create_marionette().execute()

    print(r"""
[InstaCrawler] Verifying login...
""")
    command_factory.for_verify_login(\
        marionette = marionette,\
        is_manual_verification = (order == "manual_login")).execute()

    print(r"""
[InstaCrawler] Retrieving logged username...
""")
    username = command_factory.for_obtain_user_profile(marionette).execute()
    print(fr"""
[InstaCrawler] Your username has been retrieved: '{username}'.
""")
    
    print(r"""
[InstaCrawler] Retrieving list of users who follow you.
""")
    followers = []
    command_factory.for_macro_extract_followers(\
        command_factory = command_factory,\
        marionette = marionette,\
        username = username,\
        users = followers)\
            .execute()

    print(r"""
[InstaCrawler] Retrieving list of users whom you are following.
""")
    following = []
    command_factory.for_macro_extract_following(\
        command_factory = command_factory,\
        marionette = marionette,\
        username = username,\
        users = following)\
            .execute()

    print(fr"""
[InstaCrawler] Executing your order: '{order}'.
""")
    if order == "not_following_back":
        command_factory.for_export_users_not_following_back(\
            followers = followers,\
            following = following,\
            username = username).execute()

    print(r"""
[InstaCrawler] Destroying marionette...
""")
    command_factory.for_destroy_marionette(marionette = marionette).execute()

    sys.exit(0)


if __name__ == "__main__":
    main()
