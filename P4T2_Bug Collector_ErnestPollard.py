#Bug Collector
#CTI-110-0902
#Ernest Pollard
#P4T2 Bug Collecting
#Write a program that keeps a running total of bugs collected per day


totalDays = 5
totalNumberOfInsects = 0

for currentDay in range(1, totalDays + 1):
    insectsCollected = int( input("How many insects did you collect today" + \
                               str( currentDay ) + ": " ) )
    totalNumberOfInsects = totalNumberOfInsects + insectsCollected
print("\nTotal number of insects collected for all", totalDays, "days is", \
      totalNumberOfInsects)
