import logging
import unittest
from rt_with_exceptions import Runner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='tests_12_4_1.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RunnerTest(unittest.TestCase):
    logging.info('RunnerTest')

    def test_runner_exceptions(self):
        logging.info('test_runner_exceptions')

        # Check for ValueError for negative speed
        with self.assertRaises(ValueError):
            runner = Runner('Runner1', -5)  # negative speed
        logging.info("'test_runner_exceptions' executed successfully - ValueError raised for negative speed.")

        # Check for TypeError for invalid name
        with self.assertRaises(TypeError):
            runner = Runner(12, 5)  # non-string name
        logging.info("'test_runner_exceptions' executed successfully - TypeError raised for invalid name.")

if __name__ == '__main__':
    unittest.main()
