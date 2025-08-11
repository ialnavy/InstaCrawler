import sys

from dotenv import load_dotenv

from app.commands.CommandFactory import CommandFactory


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

    order = sys.argv[1]
    if order == "help":
        print("[InstaCrawler] See help below.")
        print_usage()
        sys.exit(0)

    command_factory = CommandFactory()
    marionette = command_factory.for_create_marionette().execute()

    if order == "manual_login":
        command_factory.for_macro_manual_login(command_factory = command_factory,\
                                               marionette = marionette).execute()
    elif order == "not_following_back":
        command_factory.for_macro_users_not_following_back(command_factory = command_factory,\
                                                           marionette = marionette).execute()
    
    command_factory.for_destroy_marionette(marionette = marionette).execute()

    sys.exit(0)


if __name__ == "__main__":
    main()
