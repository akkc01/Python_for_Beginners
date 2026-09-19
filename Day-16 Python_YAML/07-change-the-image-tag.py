from pathlib import Path
import re


file_path = Path("deployment.yaml")
new_image = "myacr.azurecr.io/axion-api:v1.2.5"


# Read file
content = file_path.read_text()


# Replace image
content = re.sub(
    r"image:\s*.*",
    f"image: {new_image}",
    content
)

# Write updated content
file_path.write_text(content)

print(f"Image updated to: {new_image}")