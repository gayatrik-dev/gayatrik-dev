import requests

r = requests.get(
    "https://learn.microsoft.com/en-us/training/paths/az-400-work-git-for-enterprise-devops/"
)
print(r.status_code)
print(r.ok)
