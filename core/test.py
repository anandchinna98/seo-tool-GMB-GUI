import unittest
from core.models import Sites,create_record

class TestSiteModel(unittest.TestCase):
    def test_create_record(self):
        site=Sites(name="test", url="www.test.com",keywords="test", cities="chennai")
        create_record(site)
        self.assertIsInstance(site,Sites)

if __name__=="__main__":
    TestSiteModel()