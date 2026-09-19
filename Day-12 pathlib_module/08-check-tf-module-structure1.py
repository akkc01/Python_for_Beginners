from pathlib import Path

def test_network_module_exists():
    module = (
        Path("terraform")
        / "modules"
        / "environment"
    )
    assert module.exists()
    assert module.is_dir()
    assert (module / "main.tf").exists()