import requests
import json
import random
from flask import Flask, request
import os

app = Flask(__name__)

token = os.environ.get("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

@app.route("/random", methods=["GET"])
def call_api():
    params = {
        "q": f"language:{request.args.get("language")} is:public",
        "per_page": 50
    }
    response = requests.get("https://api.github.com/search/repositories", headers=headers, params=params)
    if response.status_code == 200:
        user_data = response.json()
        random_index=random.randint(0,49)
        item=user_data["items"][random_index]
        name=item["name"]
        description=item["description"]
        stars=item["stargazers_count"]
        forks=item["forks_count"]
        issues=item["open_issues_count"]
        return_data={
            "name":item["name"],
            "description":item["description"],
            "stars":item["stargazers_count"],
            "forks":item["forks_count"],
            "open_issues":item["open_issues_count"]
        }
        return json.dumps(return_data)
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__=="__main__":
    app.run()