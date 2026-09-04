import unittest
from servicewatch import changed

class ServiceWatchTests(unittest.TestCase):
    def test_changed(self): self.assertEqual(changed({"api":"up","web":"up"},{"api":"down","db":"up"}), {"added":["db"],"removed":["web"],"changed":["api"]})

if __name__ == "__main__": unittest.main()
