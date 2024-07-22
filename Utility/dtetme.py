import datetime
from datetime import timedelta
today = datetime.date.today()
format_date = today.strftime("%d%m%Y")
print(format_date)



# Get the current time
current_time = datetime.datetime.now()

# Calculate the time 2 minutes in advance
time_2_min_advance = current_time + timedelta(minutes=1)

formatted_time = time_2_min_advance.strftime("%I:%M %p")

print(formatted_time)

# # Print the time 2 minutes in advance
# print(time_2_min_advance.time())