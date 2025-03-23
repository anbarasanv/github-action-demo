import os
import sys
from script import addition


sys.path.insert(0, os.getcwd())


def test_data_type():
    subj = addition(2, 3)
    assert isinstance(subj, int)
