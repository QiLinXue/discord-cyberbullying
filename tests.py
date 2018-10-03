import unittest

# Import Test Modules
from client.tests import testClear, testSimpleFilter

# Combine all tests and run
if __name__ == '__main__':

    # Select classes to Run
    test_classes_to_run = [testClear.TestClear,
                           testSimpleFilter.TestSimpleFilter
                          ]

    # Load the tests
    loader = unittest.TestLoader()

    # Iterate through classes
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    # Combined Suite
    combined_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()

    runner.run(combined_suite)
