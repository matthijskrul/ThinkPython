time_now = int(input("What is the current hour?"))
time_wait = int(input("In how many hours should the alarm go off?"))
alarm_time = (time_now + time_wait) % 24
print("The clock time when the alarm will go off will be", alarm_time)