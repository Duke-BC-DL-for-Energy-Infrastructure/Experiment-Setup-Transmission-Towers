import os
from typing import List

# Paths to the train and test csv files
TRAIN_CSV_PATH = os.path.join('data', 'train_sample.csv')
TEST_CSV_PATH = os.path.join('data', 'test_sample.csv')

# Path to images_to_ignore.txt
IMAGES_TO_IGNORE_PATH = os.path.join('data', 'images_to_ignore.txt')

# Names of the .txt files
TRAIN_IMG_FNAME = 'training_img_paths.txt'
TRAIN_LBL_FNAME = 'training_lbl_paths.txt'
VALID_IMG_FNAME = 'val_img_paths.txt'
VALID_LBL_FNAME = 'val_lbl_paths.txt'

# Names of the .data files
BASELINE_DATA_FNAME = 'baseline.data'
ADDING_SYNTHETIC_DATA_FNAME = 'adding_synthetic.data'

# Names of the folders for the baseline and adding synthetic
BASELINE_FOLDER_NAME = 'baseline'
ADDING_SYNTHETIC_FOLDER_NAME = 'adding_synthetic'

# Default cross and within domain region pairs
DEFAULT_REGION_PAIRS: List[List[str, str]] = [['EM', 'EM'], ['EM', 'NE'], ['EM', 'NW'], ['EM', 'SW'],
                                              ['NE', 'EM'], ['NE', 'NE'], ['NE', 'NW'], ['NE', 'SW'],
                                              ['NW', 'EM'], ['NW', 'NE'], ['NW', 'NW'], ['NW', 'SW'],
                                              ['SW', 'EM'], ['SW', 'NE'], ['SW', 'NW'], ['SW', 'SW']]

# Default amounts of real and synthetic images
DEFAULT_RATIOS: List[List[int, int]] = [[100, 75]]
