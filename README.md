# Project Name: `JIRA Branch Name Generator`

## Description

The `JIRA Branch Name Generator` is a Python-based tool designed to simplify the process of generating meaningful branch names for GitHub repositories based on JIRA ticket information. It streamlines the creation of Git branches by converting JIRA ticket numbers and titles into standardized branch names.

## Features

1. **Input Parsing:** Accepts command-line inputs for JIRA ticket number (`-t`) and title (`-d`).
2. **Branch Name Generation:** Utilizes the provided JIRA ticket information to create a descriptive branch name.
3. **Character Limit Handling:** Ensures the generated branch name adheres to a specified character limit, preventing excessively long names.
4. **Git Command Output:** Displays the Git command for creating the branch.
5. **Clipboard Integration:** Copies the generated branch name to the system clipboard for easy pasting into the terminal.

## How to Use

1. Install the tool globally using the provided packaging mechanism.
2. Run the tool from the command line, providing the JIRA ticket number (`-t`) and title (`-d`).
3. Copy the generated Git command from the output, ready to create a new branch.

## Dependencies

- `argparse`: Handles command-line argument parsing.
- `pyperclip`: Enables clipboard interaction for copying the generated branch name.

## Project Structure

- `branch_name.py`: The main script file containing the logic for branch name generation.
- `setup.py`: Configuration file for packaging the project.
- `venv/`: Virtual environment directory to isolate dependencies.
- `dist/`: Directory containing the distributable package.

## Usage Example

```bash
$ generate-bn -t "BBR-142" -d "Replace linkedin with youtube in social icon bar"
Branch name generated and copied to clipboard:
git checkout -b bbr-142-replace-linkedin-with-youtube-in-social-icon-bar
```
