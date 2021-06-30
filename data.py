import os
from configurations import *
from typing import Dict, List
import csv


def load_data() -> Dict[str, List[str]]:
    """

    :return:
    Right now thinking it should return a dictionary in format {'region' : [list of images in region]}
    e.g. {'SW': [Arizona_id_302392_459, Arizona_id_306003_515, ...], 'NE': [Pennsylvania_id_129442_57, ...], ...}
    """

    assert os.path.isfile(TRAIN_CSV_PATH), f'TRAIN_CSV_PATH: {TRAIN_CSV_PATH} is not a valid file'
    assert os.path.isfile(TEST_CSV_PATH), f'TEST_CSV_PATH: {TEST_CSV_PATH} is not a valid file'
    assert os.path.isfile(IMAGES_TO_IGNORE_PATH), f'IMAGES_TO_IGNORE_PATH: {IMAGES_TO_IGNORE_PATH} is not a valid file'

    images_to_ignore = []

    with open(IMAGES_TO_IGNORE_PATH, 'r') as f:
        for line in f:
            image_basename = line.replace('\n', '')
            images_to_ignore.append(image_basename)

    with open(TRAIN_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        fields = csvreader.__next__()
        print(fields)

        for row in csvreader:
            break


if __name__ == '__main__':
    load_data()