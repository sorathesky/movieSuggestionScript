#!/usr/bin/python3

weekday = False
vacation = False




def sleep_in(weekday, vacation):
  if not weekday or vacation:
      return 1
  else:
      return 0


print(sleep_in(weekday, vacation))
if sleep_in(weekday, vacation) == 1:
    print ("sleep In")
else:
    print ("Don't sleep in!")