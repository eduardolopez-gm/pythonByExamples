# Write a program
# that will ask for a
# number of days
# and then will
# show how many
# hours, minutes
# and seconds are
# in that number of
# days.

days = int(input('Enter a number of days: '))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('In', days,'days\n there is', hours,'hours\n',minutes,'minutes\n',seconds,'seconds\n')