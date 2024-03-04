import pytest


@pytest.mark.smoke
def buildCheck_ios():
    print("Build is ready to test")


@pytest.mark.skip
def testCaseThree():
    print("Test Case 3: Executed")


def testCaseFour():
    print("Test Case 4: Executed")


@pytest.mark.xfail
def testCaseFive():
    print("Test Case 5: Executed")
