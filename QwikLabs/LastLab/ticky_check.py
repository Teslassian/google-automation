#!/usr/bin/env python3

import re

import operator

import csv

num_err_messages = {}

num_user_entries = {}

with open("syslog.log") as file:
 for line in file.readlines():
  if re.search(r"ERROR", line): 

   find = re.search(r"([\w.]+).$", line)
   username = find[0][0:len(find[0])-1]
   print("error username: " + username)

   if username in num_user_entries.keys():
    num_user_entries[username][1] += 1
   else:
    num_user_entries[username] = [0,1]   

   error = re.search(r" ([A-Z][a-z ']+) ", line)
   error = error[0].strip()
   if error in num_err_messages.keys():
    num_err_messages[error] += 1
   else:
    num_err_messages[error] = 1

  if re.search(r"INFO", line):
   
   find = re.search(r"([\w.]+).$", line)
   username = find[0][0:len(find[0])-1]
   print("info username: " + username)

   if username in num_user_entries.keys():
    num_user_entries[username][0] += 1
   else:
    num_user_entries[username] = [1,0]

num_err_messages = sorted(num_err_messages.items(), key=operator.itemgetter(1), reverse = True)

num_user_entries = sorted(num_user_entries.items())

print(num_err_messages)

print(num_user_entries)

with open("error_message.csv", "w", newline='') as file:
 writer = csv.writer(file)
 writer.writerow(["Error","Count"])
 writer.writerows(num_err_messages)

with open("user_statistics.csv", "w", newline='') as file:
 writer = csv.writer(file)
 writer.writerow(["Username","INFO","ERROR"])
 for key,value in num_user_entries:
  writer.writerow([key,value[0],value[1]])