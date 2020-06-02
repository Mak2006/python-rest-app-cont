import unittest

# checks the add service is working correctly


class AddTest(unittest.TestCase):
    # init
    @classmethod
    def setUpClass(cls):
        pass

    # clean up
    @classmethod
    def tearDownClass(cls):
        pass

    # test init
    def setUp(self):
        pass

    # test clean up
    def tearDown(self):
        pass

    # test method
    def test_equal(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
