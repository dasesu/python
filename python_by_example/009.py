#009
#Write a program
#that will ask for a
#number of days
#and then will
#show how many
#hours, minutes
#and seconds are
#in that number of
#days


days = int(input("input a number of days"))
hours = days*24
minutes = hours*60
seconds = minutes*60
print( "in", days," there are ", 24*days, " hours,", 24*60*days, "minuts, and ", 24*60*60*days ,"seconds")