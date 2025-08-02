import pytest
import pandas as pd
import os
from sklearn.model_selection import train_test_split

@pytest.fixture(scope="session")
def dataset():
    project_path = './'
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data

def test_DataSetType(dataset):
    #Test that dataset is a pandas dataframe
    assert isinstance(dataset, pd.DataFrame)
    pass

def test_NumberOfColumns(dataset):
    #Test to check dataset has the expected number of columns
    assert dataset.shape[1] == 15
    pass

def test_TrainingTestType(dataset):
    #Test check the training sets retains the correct dtype after splitting
    train, test = train_test_split(dataset, test_size = .10)
    assert isinstance(train, pd.DataFrame)
    pass



