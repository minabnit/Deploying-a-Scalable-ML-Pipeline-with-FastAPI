import pytest
import pandas as pd
import os

@pytest.fixture(scope="session")
def dataset():
    project_path = './'
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data

def test_NumberOfColumns(dataset):
    assert dataset.shape[1] == 15
    pass


# TODO: implement the second test. Change the function name and input as needed
#def test_two():
    #"""
    # add description for the second test
    #"""
    # Your code here
#    pass


# TODO: implement the third test. Change the function name and input as needed
#def test_three():
    #"""
    # add description for the third test
    #"""
    # Your code here
#    pass
