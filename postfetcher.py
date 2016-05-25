import praw
settings = open("settings.txt", "r")
lines = settings.readlines()
if len(lines) == 2:
	print "Checking Login information...." +  '\n'
	print "Logging in. using username " + lines[1]
	settings.close()
else:
	settings.close()
	write = open("settings.txt", "w+")
	print "You gotta enter the infromation for further use"
	username = raw_input("Enter your reddit username: ")
	write.write(username + '\n')
	password = raw_input("Enter your reddit password: ")
	write.write(password + '\n')
	write.close()

#creating the reddit object
reddit = praw.Reddit(user_agent = "automator by /u/holybananas666")	
ent_subr = raw_input("Enter the subreddit...")
subre = reddit.get_subreddit(ent_subr)
store = open("subreddit.txt", "w+")
for submission in subre.get_hot(limit = 10):
	print submission
	store.write(str(submission))
	store.write('\n\n\n')
	store.write(submission.selftext.encode('utf-8'))
	store.write('\n\n\n')
	store.write("###################### NEXT SUBMISSION ##########################")
	store.write('\n')
	store.write('\n')
store.close()	



