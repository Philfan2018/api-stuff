import requests

def get_space_launches(new_or_old):
  Space_launch_url = f"https://lldev.thespacedevs.com/2.3.0/launches/{new_or_old}/?format=json"
  response = requests.get(Space_launch_url)
  if response.status_code == 200:
    Launch_data = response.json()
    return Launch_data
  else:
    print(f"Something went wrong! {response.status_code}")

get_space_launches("upcoming")


space_launches_data = get_space_launches("upcoming")  # Call the function to get the data
print(space_launches_data.keys())  # Now access the keys of the returned dictionary

# use the next key
# prints out a url, use it as a new variable

Next_space_launches = space_launches_data["results"]

# This next part was made with the help of AI
import datetime as dt

launch_time = []
for launch in Next_space_launches:
  launch_time.append(launch["net"])
  launch_datetime = dt.datetime.fromisoformat(launch["net"].replace('Z', '+00:00'))
  launch_time.append(launch_datetime)  # Add to the list

from datetime import datetime
import pytz

est = pytz.timezone("US/Eastern")

def convert_date(launch_time):
    utc_time = datetime.strptime(launch_time, "%Y-%m-%dT%H:%M:%SZ")
    est_time = utc_time.replace(tzinfo=pytz.utc).astimezone(est)
    return est_time.strftime("%m-%d-%Y %I:%M %p %Z")

# Convert all date strings in the list
formatted_dates = [convert_date(launch["net"]) for launch in Next_space_launches]

for i, launch in enumerate(Next_space_launches):
  print(launch["name"])
  print(launch["status"]["name"])
  print(formatted_dates[i])