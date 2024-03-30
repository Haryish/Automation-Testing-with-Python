import pytest
from pyTestLogging.BaseClass import BaseClass


@pytest.mark.smoke
def buildCheck_android(initiateBuild):
    print("Test Case 0.1: Done")


class TestScenario_1(BaseClass):

    def testCase_1_1(self):
        log = self.test_LogMaking()
        print("Executing Test Case 1.1")
        log.info("Test Case 1.1: Done")

    def testCase_1_2(self):
        print("Test Case 1.2: Done")

    def testCase_1_3(self):
        print("Test Case 1.3: done")
