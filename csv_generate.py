#!/usr/bin/env python2
import csv
import codecs

input_file = "part-r-00000"

error_csv = "error_rankings.csv"
user_csv = "user_logs.csv"

error_data = []
user_data = []

with codecs.open(input_file, "r", "utf-8") as file:
	lines = file.readlines()

processing_errors = False
processing_users = False

for line in lines:
	line = line.strip()

	if "### Error Rankings ###" in line:
		processing_errors = True
		processing_users = False
		continue
	elif "### User Usage Statistics ###" in line:
		processing_errors = False
		processing_users = True
		continue

	if not line:
		continue

	parts = line.rsplit("\t", 1)
	if len(parts) != 2:
		continue

	text, count =  parts[0], parts[1]

	if processing_errors:
		error_data.append([text, count])
	elif processing_users:
		if "_" in text:
			user, log_type = text.rsplit("_", 1)
			user_data.append([user, log_type, count])

with codecs.open(error_csv, "w", "utf-8") as file:
	writer = csv.writer(file, lineterminator="\n")
	writer.writerow(["Error Message", "Count"])
	writer.writerows(error_data)

with codecs.open(user_csv, "w", "utf-8") as file:
	writer = csv.writer(file, lineterminator="\n")
	writer.writerow(["Username", "LogType", "Count"])
	writer.writerows(user_data)

print("CSV files generated successfully!")
