import unittest

if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1).run(test_suite)