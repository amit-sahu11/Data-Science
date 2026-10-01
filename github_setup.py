import subprocess
import urllib.request
import json
import sys

def get_git_token():
    p = subprocess.Popen(
        ['git', 'credential', 'fill'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = p.communicate(input="protocol=https\nhost=github.com\n")
    token = None
    username = None
    for line in stdout.splitlines():
        if line.startswith('password='):
            token = line.split('=', 1)[1]
        elif line.startswith('username='):
            username = line.split('=', 1)[1]
    return username, token

def create_github_repo(token, repo_name="Data-Science"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Python-Git-Automation"
    }
    
    # 1. Check if repo already exists
    check_url = f"https://api.github.com/repos/amit-sahu11/{repo_name}"
    check_req = urllib.request.Request(check_url, headers=headers)
    try:
        with urllib.request.urlopen(check_req) as resp:
            print(f"Repository {repo_name} already exists on GitHub!")
            return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Repository {repo_name} does not exist yet. Creating...")
        else:
            print(f"HTTPError checking repo: {e.code} {e.reason}")
            return False

    # 2. Create repo
    create_url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": repo_name,
        "description": "Comprehensive Data Science & Machine Learning Coursework, Practice Sets, Study Notes, and Progress Tracking.",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }).encode("utf-8")
    
    create_req = urllib.request.Request(create_url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(create_req) as resp:
            data = json.loads(resp.read().decode())
            print(f"Successfully created GitHub repository: {data.get('html_url')}")
            return True
    except urllib.error.HTTPError as e:
        print(f"Failed to create repo: {e.code} {e.read().decode()}")
        return False

def setup_git_and_push(repo_name="Data-Science"):
    # Run git commands
    cmds = [
        ["git", "init"],
        ["git", "config", "user.name", "Amit Kumar Sahu"],
        ["git", "config", "user.email", "sahuamitsahu87@gmail.com"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "remove", "origin"], # In case it exists
        ["git", "remote", "add", "origin", f"https://github.com/amit-sahu11/{repo_name}.git"],
        ["git", "add", "."],
        ["git", "status"],
        ["git", "commit", "-m", "Initial commit: Complete Data Science coursework, practice sets, notes & progress tracker"],
        ["git", "push", "-u", "origin", "main"]
    ]
    
    for cmd in cmds:
        print(f"Running: {' '.join(cmd)}")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.stdout:
            print(res.stdout)
        if res.stderr and "fatal: No such remote 'origin'" not in res.stderr:
            print(f"stderr: {res.stderr}")
        if cmd[1] in ["push"] and res.returncode != 0:
            print("Push failed!")
            return False
    return True

if __name__ == "__main__":
    user, token = get_git_token()
    if not token:
        print("Error: Could not retrieve GitHub credentials from Git Credential Manager.")
        sys.exit(1)
    print(f"Found credentials for user: {user}")
    
    success = create_github_repo(token, "Data-Science")
    if success:
        setup_git_and_push("Data-Science")
