from application.application import Application
import argparse


def main():
    application = Application()

    parser = argparse.ArgumentParser(prog="UserStory Manager", description="A program for managing user stories for a project")
    parser.add_argument('action', nargs=1, help="The action you want to take", choices=["ls", "list", "add"])
    parser.add_argument("--desc", "-d", help="Whether the results should be sorted descending", default=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    print(args)
    if "ls" in args.action or "list" in args.action:
        application.get_all_stories(args.desc)
    elif "add" in args.action:
        pass
        


if __name__ == "__main__":
    main()
