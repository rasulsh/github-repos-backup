import requests
import os

url          = "https://api.github.com/user/repos?per_page=300"
github_token = 'TOKEN_HERE'

#clone dir on local machine
clone_dir    = "C:\\Users\\YOUR-USERNAME\\Desktop\\backup-github"
os.chdir(clone_dir)


payload = ""
headers = {
  'Authorization': 'Bearer ' + github_token,
}
response = requests.request("GET", url, headers=headers, data=payload)

for repo in response.json():
  result = os.system("git clone " + repo['ssh_url'])
  if (result == 0):
    print("Cloned " + repo['name'])
  else:
    print("Failed to clone " + repo['name'])
  print("---------------------------------")


# Double check that the repos are cloned
for repo in response.json():
  if not os.path.isdir(clone_dir + "\\" + repo['name']):
    print("Repo " + repo['name'] + " is not exist")