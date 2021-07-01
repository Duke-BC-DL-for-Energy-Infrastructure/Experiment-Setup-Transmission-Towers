import os
from configurations import *
from typing import Dict, List
import csv


def load_data() -> Dict[str, List[str]]:
    """

    :return:
    Will return a dictionary in format {'region' : [list of images in region]}
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

    # Read train images
    train_images = {region: [] for region in REGION_NAMES}
    with open(TRAIN_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        for idx, row in enumerate(csvreader):
            id, state, region = row[0], row[3], row[4]
            image_basename = state + '_id_' + id + '_' + str(idx)
            if image_basename not in images_to_ignore:
                train_images[region].append(image_basename)

    # Read test images
    test_images = {region: [] for region in REGION_NAMES}
    with open(TEST_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        for idx, row in enumerate(csvreader):
            id, state, region = row[0], row[3], row[4]
            image_basename = state + '_id_' + id + '_' + str(idx)
            if image_basename not in images_to_ignore:
                test_images[region].append(image_basename)

    return train_images, test_images


if __name__ == '__main__':
    load_data()
