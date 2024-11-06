# suite_12_3.py
import unittest

# Import the test classes from tests_12_3.py
from tests_12_3 import RunnerTest, TournamentTest

# Create a TestSuite
test_suite = unittest.TestSuite()

# Load tests from the test classes
# test_suite.addTest(unittest.makeSuite(RunnerTest))        deprecated
# test_suite.addTest(unittest.makeSuite(TournamentTest))    deprecated
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Create a TextTestRunner with verbosity=2
runner = unittest.TextTestRunner(verbosity=3)
runner.run(test_suite)
