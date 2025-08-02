import sys
from dotenv import load_dotenv

from app.MacroManualLogin import MacroManualLogin
from app.MacroUsersNotFollowingBack import MacroUsersNotFollowingBack


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
    elif order == "manual_login":
        MacroManualLogin().execute()
    elif order == "not_following_back":
        MacroUsersNotFollowingBack().execute()
    sys.exit(0)


if __name__ == "__main__":
    main()
