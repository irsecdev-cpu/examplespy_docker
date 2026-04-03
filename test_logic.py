import os

def test_files_exist():
    assert os.path.exists("D406DOM.xml")
    assert os.path.exists("test1.py")
