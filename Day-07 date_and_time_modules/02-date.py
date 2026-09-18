import datetime as date
import dateutil.parser

now = date.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

print("Year:", year)
print("Month:", month)
print("Day:", day)



dt1 = dateutil.parser.parse("2016-04-15T08:27:18-0500")
dt2 = date.datetime.strptime(
    "2016-04-15T08:27:18-0500",
    "%Y-%m-%dT%H:%M:%S%z"
)

print("dateutil:", dt1)
print("strptime:", dt2)



# Timezone

from datetime import datetime, timezone
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

# Modern way to get current UTC time
utc_now = datetime.now(timezone.utc)

print("UTC time:", utc_now)

# Convert UTC time to local timezone
local_now = utc_now.astimezone(local)

print("Local time:", local_now)