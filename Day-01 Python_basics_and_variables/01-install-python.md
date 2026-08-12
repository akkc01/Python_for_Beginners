## Python Installation — macOS, Linux & Windows

### 🍎 macOS

**Option 1 — Homebrew (Recommended)**

```bash
brew install python
```

Verify:

```bash
python3 --version
pip3 --version
```

If Homebrew is not installed, install it first from [Homebrew](https://brew.sh/?utm_source=chatgpt.com).

**Option 2 — Official Installer**

Download Python from [Python.org](https://www.python.org/downloads/macos/?utm_source=chatgpt.com) and install the `.pkg` file.

Verify:

```bash
python3 --version
```

---

### 🐧 Linux

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

Verify:

```bash
python3 --version
pip3 --version
```

#### RHEL / CentOS / Rocky / AlmaLinux

```bash
sudo dnf install python3 python3-pip -y
```

Verify:

```bash
python3 --version
pip3 --version
```

#### Fedora

```bash
sudo dnf install python3 python3-pip -y
```

Verify:

```bash
python3 --version
pip3 --version
```

---

### 🪟 Windows

**Option 1 — Official Installer (Recommended)**

Download Python from [Python.org Windows Downloads](https://www.python.org/downloads/windows/?utm_source=chatgpt.com).

During installation, **check:**

```text
☑ Add python.exe to PATH
```

Then click **Install Now**.

Verify in PowerShell or CMD:

```powershell
python --version
pip --version
```

**Option 2 — winget**

```powershell
winget install Python.Python.3
```

Verify:

```powershell
python --version
pip --version
```

### Quick Summary

| OS            | Recommended Installation                              |
| ------------- | ----------------------------------------------------- |
| macOS         | `brew install python`                                 |
| Ubuntu/Debian | `sudo apt install python3 python3-pip -y`             |
| RHEL/Fedora   | `sudo dnf install python3 python3-pip -y`             |
| Windows       | Official installer / `winget install Python.Python.3` |
