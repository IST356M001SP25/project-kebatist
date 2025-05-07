# tests/test_utils.py

'''from utils import save_json, load_json, save_clean_csv, load_clean_csv

# Test paths
RAW_PATH = os.path.join("cache", "raw_data.json")
CLEAN_PATH = os.path.join("cache", "clean_data.csv")

# Sample data
sample_data = {"name": "Inception", "rating": 8.8, "year": 2010}
sample_df = pd.DataFrame({"name": ["Inception", "Avatar"], "rating": [8.8, 7.8], "year": [2010, 2009]})

# Correct test function names
def test_save_and_load_json():
    save_json(sample_data, RAW_PATH)
    loaded_data = load_json(RAW_PATH)
    assert loaded_data == sample_data, "JSON save/load test failed"
def test_save_and_load_csv():
    save_clean_csv(sample_df, CLEAN_PATH)
    loaded_df = load_clean_csv(CLEAN_PATH)
    pd.testing.assert_frame_equal(loaded_df, sample_df, check_dtype=False)
    '''
# tests/test_utils.py
import sys
import os
import pytest
import pandas as pd

# Add the parent directory of utils.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import functions from utils.py
# tests/test_utils.py
from utils import save_json, load_json, save_clean_csv, load_clean_csv

# Paths for testing
RAW_PATH = "cache/raw_data.json"
CLEAN_PATH = "cache/clean_data.csv"

# Test data
sample_data = {"title": "Inception", "rating": 8.8, "year": 2010}
sample_df = pd.DataFrame({"title": ["Inception", "Avatar"], "rating": [8.8, 7.8], "year": [2010, 2009]})

# Test JSON save/load
def test_save_json():
    save_json(sample_data, RAW_PATH)
    loaded_data = load_json(RAW_PATH)
    assert loaded_data == sample_data
def test_load_json():
    save_json(sample_data, RAW_PATH)
    loaded_data = load_json(RAW_PATH)
    assert loaded_data == sample_data

# Test CSV save/load
def test_save_clean_csv():
    save_clean_csv(sample_df, CLEAN_PATH)
    loaded_df = load_clean_csv(CLEAN_PATH)
    pd.testing.assert_frame_equal(loaded_df, sample_df, check_dtype=False)
def test_load_clean_csv():
    save_clean_csv(sample_df, CLEAN_PATH)
    loaded_df = load_clean_csv(CLEAN_PATH)
    pd.testing.assert_frame_equal(loaded_df, sample_df, check_dtype=False)

from utils import add_numbers, multiply_numbers

def test_add_numbers():
    result = add_numbers(3, 4)
    assert result == 7

def test_multiply_numbers():
    result = multiply_numbers(3, 4)
    assert result == 12