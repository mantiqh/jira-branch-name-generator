from setuptools import setup

setup(
    name='jira-branch-name-generator',
    version='1.0.0',
    scripts=['jira_branch_name_generator.py'],
    install_requires=['argparse', 'pyperclip'],
)
