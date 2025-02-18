import pytest


# config file on test method
def testCaseOne(initiateBuild):
    print("Test Case 3.1.1: Done")


# config file on test class without scope="class" parameter
@pytest.mark.usefixtures("initiateBuild")
class TestScenario_3_2:

    def testCaseTwo(self):
        print("Test Case 3.2.1: Done")

    def testCaseThree(self):
        print("Test Case 3.2.2: Done")


# config file on test class with scope="class" parameter
@pytest.mark.usefixtures("initiateNewBuild")
class TestScenario_3_3:

    def testCaseFour(self):
        print("Test Case 3.3.1: Done")

    def testCaseFive(self):
        print("Test Case 3.3.2: Done")

    def testCaseSix(self):
        print("Test Case 3.3.3: Done")
