import os
import requests

repo_owner = "RishitaChourey"
repo_name = "CodeBites_PS_2.1.1"
github_token = os.environ['GITHUB_TOKEN']

def fetch_open_issues():
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    issues = response.json()
    return [issue for issue in issues if issue['state'] == 'open']

def generate_statement(issue):
    return f"Hi there! Issue #{issue['number']} is still open. We are looking forward to your response."

if __name__ == "__main__":
    open_issues = fetch_open_issues()
    for issue in open_issues:
        statement = generate_statement(issue)
        print(statement)
