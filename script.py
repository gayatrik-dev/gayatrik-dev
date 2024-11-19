import sys
import requests
import os


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


print(greet("World"))
print(greet("Gayatri"))

r = requests.get(
    "https://learn.microsoft.com/en-us/training/paths/az-400-work-git-for-enterprise-devops/"
)
print(r.status_code)
