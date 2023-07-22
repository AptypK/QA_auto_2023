import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()
        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()
        return body

    # Personal API-test tasks - Project task #4

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()
        return body

    def get_commit(self, owner, repo, commit_sha):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}"
        )
        body = r.json()
        return body
