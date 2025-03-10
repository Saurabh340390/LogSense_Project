#!usr/bin/env python2

import random
import time
from datetime import datetime, timedelta

messages = ["INFO", "ERROR"]
successes = ["Created ticket", "Closed ticket", "Commented on ticket"]
errors = ["Timeout while retrieving information", "The ticket was modified while updating", 
	  "Connection to DB failed", "Tried to add information to a closed ticket", 
	  "Tried to add information to a closed ticket", "Permission denied while closing ticket",
	  "Ticket doesn't exist"]
usernames = ["mcintosh", "breee", "ac", "mdouglas", "blossom", "rr.robinson", "oren", "jackowens"]

log_lines = []
ticket_id = 999
for _ in range (1000):
	message = random.choice(messages)
	username = random.choice(usernames)
	timestamp = (datetime.now() - timedelta(seconds=random.randint(0,86400))).strftime("%b %d %H:%M:%S")

	if message == "INFO" :
		ticket_id += 1
		success = random.choice(successes)
		log_line = "{0} ubuntu.local ticky: {1} {2} [#{3}] ({4})".format(timestamp, message, success, ticket_id, username)
	else :
		error = random.choice(errors)
		log_line = "{0} ubuntu.local ticky: {1} {2} ({3})".format(timestamp, message, error, username)

	log_lines.append(log_line)

with open("system_logs.log", "w") as syslog :
	syslog.write("\n".join(log_lines))

print("Log file 'system_logs.log' is generated successfully!")
