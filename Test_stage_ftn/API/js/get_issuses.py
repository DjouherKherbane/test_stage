from github import Github
import json

g = Github("19e324d47f08e8481e37ccaa704ce94c030bbcc1")

repo = g.get_repo("PyGithub/PyGithub")

open_issues = repo.get_issues(state='open')

data = {"issues":[]}

with open("data.json", "r+") as outfile:
 for issue in open_issues:
  data["issues"].append({"title":issue.title,"number":issue.number})
  outfile.seek(0)
  json.dump(data, outfile)


