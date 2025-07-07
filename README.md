# 🔀 Random GitHub Repository API

This is a simple [Flask](https://flask.palletsprojects.com/en/stable/) application that uses the [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) to fetch a **random public repository** based on a specified programming language.

## 🚀 Features

* Fetches 50 public repositories matching a language query
* Randomly selects one repository from the list
* Returns JSON with:

  * `name`
  * `description`
  * `stars`
  * `forks`
  * `issues(pull requests and open issues)`

## 📦 Requirements

* Python 3.7+
* GitHub Personal Access Token

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/DragonSenseiGuy/random-repo-api.git
   cd random-repo-api
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip3 install requirements.txt
   ```

4. **Set your GitHub token as an environment variable**

   ```bash
   export GITHUB_TOKEN=your_personal_access_token  # On Windows: set GITHUB_TOKEN=...
   ```

## ▶️ Usage

Start the Flask app:

```bash
python main.py
```

Then make a GET request to:

```
http://127.0.0.1:500/random?language=python
```

Replace *python* with any programming language of your choice.

## 🧪 Sample Response

```json
{
  "name": "awesome-python",
  "description": "A curated list of awesome Python frameworks, libraries, software and resources",
  "stars": 168000,
  "forks": 22000,
  "open_issues": 120
}
```

## 🔒 Notes

* Make sure your GitHub token has access to the [Search API](https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories), but no special scopes are required.
* Rate limiting applies as per [GitHub’s API policy](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28).

## 📄 License

[MIT License](LICENSE)

