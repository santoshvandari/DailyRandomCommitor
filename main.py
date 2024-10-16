from github import Github
from datetime import datetime
import os

# Get today's date in string format
today_date = datetime.today().strftime("%Y-%m-%d")

# Get GitHub API key from environment variable
api_key = os.environ['API_KEY']
github = Github(api_key)

# Set the repository and username
username = "santoshvandari"
repo = github.get_repo(f"{username}/DailyRandomCommitor")

# Path to the file
file_path = "listofcommitdate.txt"
try:
        # Try to retrieve the file content
        file = repo.get_contents(file_path)
        file_content = file.decoded_content.decode("utf-8")
        
        # Append the new date to the existing content
        updated_content = f"{file_content}\nToday Date: {today_date}"
        
        # Update the file in the repository
        repo.update_file(
            path=file_path,
            message=f"Commit on {today_date}.",
            content=updated_content,
            sha=file.sha
        )
        print(f"Appended date: {today_date}")
        
except Exception as e:
        # If the file does not exist, create it
        if str(e).startswith("404"):
            initial_content = f"Today Date: {today_date}"
            repo.create_file(
                path=file_path,
                message=f"Create and commit date: {today_date}",
                content=initial_content
            )
            print(f"Created file and committed date: {today_date}")
        else:
            print(f"Failed to append file on {today_date}. Error: {e}")
