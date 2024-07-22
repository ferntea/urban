import logging
import unittest
from rt_with_exceptions import Runner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='tests_12_4.log',  # file name is changed
    filemode='w',  # in the task it is recommended 'r', which is not common
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'  # timestamp - importance - message
)


class RunnerTest(unittest.TestCase):
    logging.info('RunnerTest')

    def test_runner_exceptions(self):
        logging.info('test_runner_exceptions')

        # Test for ValueError when negative speed is provided
        try:
            runner = Runner('Runner1', -5)  # negative speed
        except ValueError as e:
            logging.info("'test_runner_exceptions' executed successfully - ValueError raised for negative speed.")
        else:
            self.fail("ValueError not raised for negative speed")  # Fail the test if no exception is raised

        # Test for TypeError when invalid name is provided
        try:
            runner = Runner(12, 5)  # invalid name
        except TypeError as e:
            logging.info("'test_runner_exceptions' executed successfully - TypeError raised for invalid name.")
        else:
            self.fail("TypeError not raised for invalid name")  # Fail the test if no exception is raised


if __name__ == '__main__':
    unittest.main()
