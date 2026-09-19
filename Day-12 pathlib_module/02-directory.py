from pathlib import Path

# cwd
current_dir = Path.cwd()
print(current_dir)


# user home directory
from pathlib import Path
home = Path.home()
print(home)


# parent directory
path = Path("/home/user/project")
print(path.parent)
print(path.parent.parent)


# create a directory
from pathlib import Path
directory = Path("terraform")
directory.mkdir(parents=True, exist_ok=True )


# create a nested directory
from pathlib import Path
path = Path("/Users/amitkumar/Documents/Study-Akkc/Python/Day-12 pathlib_module/pathlib")
path.mkdir(parents=True, exist_ok=True )


# create a nested directory if already exist
from pathlib import Path
path = Path("/Users/amitkumar/Documents/Study-Akkc/Python/Day-12 pathlib_module/pathlib-01")
path.mkdir(parents=True, exist_ok=True )


# delete an empty dir
directory = Path("/Users/amitkumar/Documents/Study-Akkc/Python/Day-12 pathlib_module/pathlib-01")
directory.rmdir()
#rmdir() only works when the directory is empty.


from pathlib import Path
project_dir = Path.cwd()
terraform_dir = project_dir / "terraform"
print(terraform_dir)

if not terraform_dir.exists():
    print("Terraform directory not found")
    