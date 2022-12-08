[list of stories](/list.png)
[example of writing a story](/story.png)
# User Stories TUI (almost)
The aim of this project was to create a functional app using Python. Originally I wanted to create a full blown TUI using [Textual](https://github.com/Textualize/textual)but decided to go simple and just keep it as a CLI tool using the similar package [Rich](https://github.com/Textualize/rich).

## Purpose
The purpose of the app is to make writing and storing [user stories](https://www.atlassian.com/agile/project-management/user-stories) easy.

## How to use
1. Clone the repo
2. Install dependencies `pip install -r requirements.txt`
3. Run the app with `python3 src/main.py {command}`

## Commands
- `ls` - List all saved user stories (optionally add `-d` to sort by descending scores)
- `add` - Add a new user story
- `del` - Delete a saved user story
- `clear` - Delete all saved user stories
