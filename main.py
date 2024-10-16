from github import Github
from datetime import datetime
import os

today_date = datetime.today().strftime("%Y-%m-%d")

api_key = os.environ['api_key']
github = Github(api_key)

username = "santoshvandari"
repo = github.get_repo(f"{username}/DailyRandomCommitor")

for i in range(8):
    file_path = "listofcommitdate.txt"
    file_content = f"Today Date : {today_date}"
    
    try:
        repo.create_file(
            path=file_path,
            message= f"Commit date: {today_date}",
            content=file_content
        )
        print(f"Commit date: {today_date}")
    except Exception as e:
        print(f"Failed to COmmit file on {today_date}. Error: {e}")