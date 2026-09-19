from pathlib import Path

path = Path("terraform/main.tf")
# Path represents a filesystem path. Creating a Path object does not create the file or directory.
# path = Path("terraform") / "main.tf"
print(path)



# chech path exist
from pathlib import Path
path = Path("/Users/amitkumar/Documents/Study-Akkc/Python/Day-12 pathlib_module/01-path.py")
print(path.exists())


# find absolute path
from pathlib import Path
path = Path("01-path.py")
print(path.absolute())
