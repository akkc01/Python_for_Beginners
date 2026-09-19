from pathlib import Path
def test_terraform_files_exist():
    terraform_dir = Path("terraform")

    assert terraform_dir.exists()
    assert terraform_dir.is_dir()
    assert (terraform_dir / "main.tf").exists()
    assert (terraform_dir / "variables.tf").exists()
    assert (terraform_dir / "outputs.tf").exists()
