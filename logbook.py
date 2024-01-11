
import os
import shutil
import argparse
from datetime import datetime

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("author")
    args = parser.parse_args()

    # Get the current date
    datetime_now = datetime.now()

    # Format the date
    formatted_date = "Log " + datetime_now.strftime("%d %b %Y")
    formatted_date_with_underscores = formatted_date.replace(" ", "_").lower()

    # Create the logs directory if it does not exist
    os.makedirs('logs', exist_ok=True)

    # Copy the template.md to a new file in the logs directory with the current date as the filename
    shutil.copy2('logs/template.md', f'logs/{formatted_date_with_underscores}.md')

    # Open the new log file and replace %DATO% and %AUTHOR% with the current date and author
    with open(f'logs/{formatted_date_with_underscores}.md', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.write(content.replace('%DATO%', datetime_now.strftime("%d %b %Y")).replace('%AUTHOR%', args.author))
        f.truncate()

    # Open the overview.md file in append mode and add a link to the new log file
    with open('logs/overview.md', 'a') as f:
        f.write(f'* [{formatted_date}](logs/{formatted_date_with_underscores}.md)\n')

if __name__ == "__main__":
    main()