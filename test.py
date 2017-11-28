from github3 import login
#import sys
g = login('palkaa123', password='password1')
palkaa123 = g.me()
print(palkaa123.name)
print('Hello')
#g = Github(sys.argv[1], sys.argv[2])

# Print information about logged in user
##print("GitHub of " + sys.argv[1] + "\n")
#print("Name: " + g.get_user().name)
#print("Public repos: " + str(g.get_user().public_repos))
#print("Disk usage: " + str(g.get_user().disk_usage))

# Print information about each repo
for repo in g.followers():
  # print (repo.name + " | Last push: " + str(repo.pushed_at))
   # print ("\tClone: " + repo.clone_url + "\n")
   print(str(repo))

