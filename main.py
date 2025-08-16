import sys

from dotenv import load_dotenv

from app.FactoryHub import FactoryHub
from marionette.UserLikeMsEdgeNav import UserLikeMsEdgeNav


# Load environment variables from .env file
load_dotenv()

available_orders = [\
    "help",\
    "manual_login",\
    "extract_followers",\
    "extract_following",\
    "not_following_back",\
    "not_following_back_complete"]

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


    print(r"""
[InstaCrawler] Initialising factory hub...
""")
    factory_hub = FactoryHub()

    print(fr"""
[InstaCrawler] Executing your order: '{order}'.
""")
    if order == "not_following_back":
        factory_hub.for_order_commands()\
            .for_users_not_following_back_order(factory_hub).execute()
    else:
        print(r"""
[InstaCrawler] Initialising marionette...
""")
        marionette = UserLikeMsEdgeNav()
        if order == "manual_login":
            factory_hub.for_marionette_commands()\
                .for_verify_login(\
                    marionette = marionette,\
                    is_manual_verification = True).execute()
        elif order == "extract_followers":
            factory_hub.for_order_commands()\
                .for_extract_followers_order(factory_hub, marionette).execute()
        elif order == "extract_following":
            factory_hub.for_order_commands()\
                .for_extract_following_order(factory_hub, marionette).execute()
        elif order == "not_following_back_complete":
            factory_hub.for_order_commands()\
                .for_users_not_following_back_complete_order(factory_hub, marionette).execute()

    sys.exit(0)


if __name__ == "__main__":
    main()
