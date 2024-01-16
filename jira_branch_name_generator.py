import argparse
import re
import pyperclip

def create_branch_name(ticket, title):
    # Remove non-alphanumeric characters and replace spaces with hyphens
    ticket = re.sub(r'[^a-zA-Z0-9]', '', ticket)
    title = re.sub(r'[^a-zA-Z0-9\s]', '', title).strip().replace(' ', '-')
    
    # Limit the length of the branch name
    max_length = 50
    branch_name = f"{ticket}-{title[:max_length-len(ticket)-1]}"
    return branch_name.lower()

def main():
    parser = argparse.ArgumentParser(description="Generate GitHub branch name from JIRA ticket.")
    parser.add_argument("-t", "--ticket", required=True, help="JIRA ticket number.")
    parser.add_argument("-d", "--title", required=True, help="JIRA ticket title.")

    args = parser.parse_args()

    branch_name = create_branch_name(args.ticket, args.title)
    git_command = f"git checkout -b {branch_name}"

    # Copy branch name to clipboard
    pyperclip.copy(git_command)

    print(f"Branch name generated and copied to clipboard:\n{git_command}")

if __name__ == "__main__":
    main()
