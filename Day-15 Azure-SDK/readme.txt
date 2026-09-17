How to setup venv--

1. Go to your project folder
	cd "/Users/amitkumar/Documents/Study-Akkc/Python/Day-11"

2. Create the virtual environment
	python3 -m venv venv

This creates:
	Day-11 Python_YAML/
    ├── venv/
    ├── PyYaml.py
    └── deployment.yaml

3. Activate the virtual environment
	source venv/bin/activate

You should now see:
	(venv) ❯

4. Verify Python is coming from the venv
    which python


5. Install it inside your venv:
    pip install azure-identity
    pip install azure-mgmt-resource
    pip install azure-mgmt-network azure-identity
    pip install azure-mgmt-managementgroups