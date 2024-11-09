seconds = int(input("Enter seconds: "))
hour = 0
minute = 0
second = 0
while seconds >= 3600:
    hour += 1
    seconds -= 3600

while seconds >= 60:
    minute +=1
    seconds -= 60

second = seconds

print(hour,":",minute,":",second)
