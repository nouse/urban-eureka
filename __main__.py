import sys
import pytest
import os.path

sys.exit(pytest.main([f"ch{i:02d}" for i in range(2, 13)]))