import pytest
from pathlib import Path
import shutil
import tempfile


@pytest.fixture
def temp_log_dir():
    """
    Create a temporary log directory for tests and clean up afterward.
    """
    dir_path = Path(tempfile.mkdtemp())
    yield dir_path
    # Cleanup after test
    shutil.rmtree(dir_path)
