import pytest


@pytest.mark.smoke
def buildCheck_android():
    print("Build is ready to test")


def testCaseOne():
    print("Test Case: 1 done")


def testCaseTwo():
    print("Test Case: 2 done")


def testScenario():
    print("Test Scenario Done")
