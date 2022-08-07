import sys
import pytest
import os.path

cwd = os.path.basename(os.getcwd())
module_name = os.path.basename(os.path.dirname(__file__))

sys.exit(pytest.main([module_name]))