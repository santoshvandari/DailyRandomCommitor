# Daily Random Commitor

This Script automatically commits the current date to a file `listofcommitdate.txt` in your GitHub repository daily using the GitHub API. If the file exists, the script appends the current date. If not, the file is created with the date.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed.
2. **GitHub Personal Access Token** with `Contents` (read and write) permission.
3. **`PyGithub` library** installed.
4. A **GitHub repository** to run the script against.

## Setup Steps

### 1. Install Required Python Packages

Install the `PyGithub` library to interact with the GitHub API:

```bash
pip install PyGithub
```

### 2. Create a Personal Access Token

1. Navigate to **GitHub** > **Settings** > **Developer Settings** > **Personal Access Tokens** > **Fine-grained Tokens**.
2. Create a new token with the following permissions:
   - **Repository** > **Contents** (Read and write).
3. Save the token for future use.

### 3. Set Up Environment Variable for API Key

The script uses an environment variable `API_KEY` to authenticate with GitHub. Set it as follows:

- **On Linux/macOS**:
  ```bash
  export API_KEY=your_github_token_here
  ```

- **On Windows (Command Prompt)**:
  ```bash
  set API_KEY=your_github_token_here
  ```

- **On Windows (PowerShell)**:
  ```powershell
  $env:API_KEY="your_github_token_here"
  ```

`Note: You can also Directly passed the API_KEY in the variables.`

### 4. Clone Your Repository

Clone or set up your GitHub repository. For example, if your username is `santoshvandari` and your repository name is `DailyRandomCommitor`, clone it using:

```bash
git clone https://github.com/santoshvandari/DailyRandomCommitor.git
```

### 5. Update the Script

In the script, ensure the following are set correctly:

- `username = "your_github_username"`
- `repo = github.get_repo(f"{username}/your_repository_name")`
- `file_path = "listofcommitdate.txt"`

### 6. Run the Script

To run the script and append the current date to `listofcommitdate.txt`, execute:

```bash
python your_script.py
```

### 7. Automate with GitHub Actions

You can automate this task using GitHub Actions. Here's how you can set up the `.github/workflows/action.yml` file to schedule the script to run daily at Specific (UTC+5:45).

There is the file called `action.yml` in `.github/workflows/` folder of the repository which you can modify according to your needs.


### 8. Store Your GitHub Token in Secrets

1. Go to your GitHub repository.
2. Navigate to **Settings** > **Secrets and Variables** > **Actions**.
3. Add a new secret named `API_KEY` with the value of your GitHub personal access token.

### Example Output

When the script runs, `listofcommitdate.txt` will either be updated or created with a new entry:

```
Today Date: 2024-10-16
```

### Error Handling

The script handles the following exceptions:

- If the file does not exist, it creates it.
- If there are other errors (e.g., API or permission errors), the script logs the error to the console.

## Contributing
We welcome contributions! Feel free to submit a pull request or open an issue if you find bugs or want to add new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
