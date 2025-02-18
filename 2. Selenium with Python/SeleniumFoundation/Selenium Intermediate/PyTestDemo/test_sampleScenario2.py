import pytest


@pytest.mark.smoke
def buildCheck_ios():
    print("Test Case 0.2: done")


@pytest.mark.skip
def testCase_2_1():
    print("Test Case 2.1: Done")


def testCase_2_2():
    print("Test Case 2.2: Done")


@pytest.mark.xfail
def testCase_2_3():
    print("Test Case 2.3: Done")
