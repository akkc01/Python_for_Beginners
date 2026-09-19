from pathlib import Path

# list all files
path = Path("terraform")
for item in path.iterdir():
    print(item)


# find .tf files
from pathlib import Path
terraform_dir = Path("terraform")
for file in terraform_dir.glob("*.tf"):
    print(file)


# recursive search
for file in Path("terraform").rglob("*.tf"):
    print(file)


# rename a file
from pathlib import Path
old_file = Path("old.txt")
old_file.rename("new.txt")


# delete a file
file = Path("test.txt")
file.unlink()
#unlink() removes a file.


# check file size 
from pathlib import Path
file = Path("main.tf")
print(file.stat().st_size)


# file meta data
info = Path("main.tf").stat()
print(info.st_size)
print(info.st_mtime)


# find all terraform files
from pathlib import Path
terraform_dir = Path("terraform")
terraform_files = list(terraform_dir.rglob("*.tf"))
for file in terraform_files:
    print(file)
