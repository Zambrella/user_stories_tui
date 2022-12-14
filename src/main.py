from application.application import Application
import argparse


def main():
    application = Application()

    parser = argparse.ArgumentParser(prog="UserStory Manager", description="A program for managing user stories for a project")
    parser.add_argument('action', help="The action you want to take", choices=["ls", "add", "del", "clear"])
    parser.add_argument("--desc", "-d", help="Whether the user stories should be sorted by sores descending instead of ascending", action="store_true")
    args = parser.parse_args()
    if "ls" in args.action or "list" in args.action:
        application.get_all_stories(args.desc)
    elif "add" in args.action:
        application.add_story()
    elif "del" in args.action:
        application.delete_story()
    elif "clear" in args.action:
        application.clear()
        


if __name__ == "__main__":
    main()
