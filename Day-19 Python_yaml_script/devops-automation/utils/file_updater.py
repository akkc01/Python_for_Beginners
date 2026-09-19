import re
from pathlib import Path


class FileUpdater:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        if not self.file_path.is_file():
            raise ValueError(
                f"Path is not a file: {self.file_path}"
            )

    def replace(self, pattern, replacement):

        # Read file
        content = self.file_path.read_text()

        # Find and replace
        updated_content, count = re.subn(
            pattern,
            replacement,
            content
        )

        # Nothing was replaced
        if count == 0:
            raise ValueError(
                f"Pattern not found: {pattern}"
            )

        # Write updated content
        self.file_path.write_text(
            updated_content
        )

        print(
            f"Updated {self.file_path} "
            f"({count} replacement(s))"
        )

        return count

    def update_server_name(self, server_name):
        return self.replace(
            r"(?m)^server_name\s*=.*$",  # WHAT_TO_FIND 
            f"server_name={server_name}" # WHAT_TO_REPLACE_WITH
        )

    def update_environment(self, environment):
        return self.replace(
            r"(?m)^environment\s*=.*$",
            f"environment={environment}"
        )

    def update_image_tag(self, image, tag):
        pattern = (
            rf"(image:\s*{re.escape(image)}:)"
            r"[^\s]+"
        )

        replacement = rf"\g<1>{tag}"

        return self.replace(
            pattern,
            replacement
        )


'''

complete regex broken into one line:
    (?m)  → Multiline mode
    ^     → Start of the line
    server_name  → Match the exact text "server_name"
    \s*   → Match zero or more spaces/tabs
    =     → Match "="
    .*    → Match any characters, zero or more times
    $     → End of the line

So the complete meaning in one sentence is:
    (?m)^server_name\s*=.*$ → In multiline mode, find the complete line that starts with server_name, followed by zero or more spaces, then =, and then any value until the end of that line.

'''