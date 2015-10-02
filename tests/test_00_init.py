from check_bacula import init
import shutil
import os


def test_00_init():
    # Remove ~/.test dir.
    testdir = os.path.join(os.path.expanduser("~"), '.test-check-bacula')
    if os.path.isdir(testdir):
        shutil.rmtree(testdir)

    cfg = init(testdir)
    assert 'localhost' in cfg.get('database', 'hostname')
