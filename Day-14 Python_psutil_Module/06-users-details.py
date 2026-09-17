import psutil

# Returns currently logged-in users.
for user in psutil.users():
    print(user)


# Returns the time when the system was booted.
print(psutil.boot_time())

# You can convert it:
from datetime import datetime
import psutil
boot_time = psutil.boot_time()
print(datetime.fromtimestamp(boot_time))


# Returns temperature sensor information on platforms where supported.
print(psutil.sensors_temperatures())


# Returns battery information where supported.
battery = psutil.sensors_battery()
print(battery)


