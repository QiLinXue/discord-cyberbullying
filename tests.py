import unittest

# Import Test Modules
from client.tests import testClassifiers

# Combine all tests and run
if __name__ == '__main__':

    # Select classes to Run
    test_classes_to_run = [
                           testClassifiers.TestClassifiers
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
