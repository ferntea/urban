import logging
import unittest
from rt_with_exceptions import Runner

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='tests_12_4_2.log',  # file name is changed
    filemode='w',  # in the task it is recommended 'r', which is not common
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'  # timestamp - importance - message
)


class RunnerTest(unittest.TestCase):
    logging.info('RunnerTest')

    def test_runner_creation_valid(self):
        runner = Runner('Runner1', 5)
        logging.info(f"Test 1 Passed: Runner created: {runner.name}, Speed: {runner.speed}")

    def test_runner_creation_invalid_name(self):
        with self.assertRaises(TypeError) as context:
            Runner(12345, 5)
        logging.info(f"Test 2 Passed: {context.exception}")

    def test_runner_creation_negative_speed(self):
        with self.assertRaises(ValueError) as context:
            Runner("Runner3", -5)
        logging.info(f"Test 3 Passed: {context.exception}")

    def test_runner_run_method(self):
        runner = Runner("Runner1", 5)
        runner.run()
        logging.info(f"Test 4 Passed: Runner {runner.name} distance after run: {runner.distance}")

    def test_runner_walk_method(self):
        runner = Runner("Runner5", 5)
        runner.walk()
        logging.info(f"Test 5 Passed: Runner {runner.name} distance after walk: {runner.distance}")

    def test_runner_equality(self):
        r1 = Runner('Runner6', 5)
        r2 = Runner('Runner6', 5)
        self.assertEqual(r1, r2)
        logging.info("Test 6 Passed: Runners are equal")

    def test_runner_equality_with_string(self):
        runner = Runner("Runner7", 5)
        self.assertEqual(runner.name, 'Runner7')
        logging.info("Test 7 Passed: Runner name matches string")


if __name__ == "__main__":
    unittest.main()
