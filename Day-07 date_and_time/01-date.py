import datetime
import dateutil.parser

dt1 = dateutil.parser.parse("2016-04-15T08:27:18-0500")
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt1)
print(dt)


# timezone

from datetime import datetime
from dateutil import tz
utc = tz.tzutc()
local = tz.tzlocal()
utc_now = datetime.utcnow()
utc_now # Not timezone-aware.
utc_now = utc_now.replace(tzinfo=utc)
utc_now # Timezone-aware.
local_now = utc_now.astimezone(local)
print(local_now)
l