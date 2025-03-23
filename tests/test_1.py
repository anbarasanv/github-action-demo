import os
import sys
from script import addition

sys.path.insert(0, os.getcwd())


def test_add():
    subj = addition(2, 3)
    assert subj == 5
