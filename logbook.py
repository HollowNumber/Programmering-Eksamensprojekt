import os
import shutil
from datetime import datetime

# Get the current date
datetime = datetime.now()

# Format the date
formatted_date = "Log " + datetime.strftime("%d %b %Y")

# Create the logs directory if it does not exist
os.makedirs('logs', exist_ok=True)

# Copy the template.md to a new file in the logs directory with the current date as the filename
shutil.copy2('template.md', f'logs/{formatted_date}.md')

# Open the overview.md file in append mode and add a link to the new log file
with open('logs/overview.md', 'a') as f:
    f.write(f'* [{formatted_date}](logs/{formatted_date}.md)\n')