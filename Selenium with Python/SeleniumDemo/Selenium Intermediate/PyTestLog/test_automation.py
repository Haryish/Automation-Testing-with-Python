import logging
import pytest
import selenium
# import baseClass


def log_details():
    logging.basicConfig(
        filename="demo.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S %p"
    )
    return logging.getLogger()


@pytest.mark.smoke
def buildCheck_android(initiateBuild):
    print("Test Case 0.1: Done")


class TestPy:
    def testCase_1_1(self):
        log = log_details()
        print("Test Case 1.1: Done")
        log.info("debugged")

    def testCase_1_2(self):
        print("Test Case 1.2: Done")

    def testCase_1_3(self):
        print("Test Case 1.3: done")
