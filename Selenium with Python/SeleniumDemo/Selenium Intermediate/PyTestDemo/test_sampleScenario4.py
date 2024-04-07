# Data Driven Fixture
import pytest


@pytest.mark.usefixtures("dataLoad")
class TestScenario_4_1:
    def testCaseOne(self, dataLoad, i=1):
        for element in dataLoad:
            print(element)
            print(f"Test Case 4.1.{i}: done")
            i += 1


@pytest.mark.usefixtures("parameter")
class TestScenario_4_2:
    def testCaseOne(self, parameter, i=1):
        print(parameter)
        print(f"Test Case 4.2.{i}: done")
        i += 1
