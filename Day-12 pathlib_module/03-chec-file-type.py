from pathlib import Path

path = Path("main.tf")
if path.is_file():
    print("It is a file")


path = Path("terraform")
if path.is_dir():
    print("It is a directory")


from pathlib import Path
path = Path("terraform")
if not path.exists():
    print("Path does not exist")
elif path.is_dir():
    print("Directory exists")
elif path.is_file():
    print("File exists")
