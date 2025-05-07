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
# Import functions from utils.py
# tests/test_utils.py
from ..code.utils import save_json, load_json, save_clean_csv, load_clean_csv

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

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b