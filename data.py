import os
from configurations import *
from typing import Dict, List
import csv


def load_real_data() -> Dict[str, List[str]]:
    """
    :return:
    Will return a dictionary in format {'region' : [list of images in region]}
    e.g. {'SW': [Arizona_id_302392_459, Arizona_id_306003_515, ...], 'NE': [Pennsylvania_id_129442_57, ...], ...}
    """

    assert os.path.isfile(TRAINING_CSV_PATH), f'TRAINING_CSV_PATH: {TRAINING_CSV_PATH} is not a valid file'
    assert os.path.isfile(VALIDATION_CSV_PATH), f'VALIDATION_CSV_PATH: {VALIDATION_CSV_PATH} is not a valid file'
    assert os.path.isfile(IMAGES_TO_IGNORE_PATH), f'IMAGES_TO_IGNORE_PATH: {IMAGES_TO_IGNORE_PATH} is not a valid file'

    images_to_ignore = []

    with open(IMAGES_TO_IGNORE_PATH, 'r') as f:
        for line in f:
            image_basename = line.replace('\n', '')
            images_to_ignore.append(image_basename)

    # Read training images
    training_images = {region: [] for region in REGION_NAMES}
    with open(TRAINING_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        for idx, row in enumerate(csvreader):
            id, state, region = row[0], row[3], row[4]
            image_basename = state + '_id_' + id + '_' + str(idx)
            if image_basename not in images_to_ignore:
                training_images[region].append(image_basename)

    # Read test images
    validation_images = {region: [] for region in REGION_NAMES}
    with open(VALIDATION_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        for idx, row in enumerate(csvreader):
            id, state, region = row[0], row[3], row[4]
            image_basename = state + '_id_' + id + '_' + str(idx)
            if image_basename not in images_to_ignore:
                validation_images[region].append(image_basename)

    return training_images, validation_images


def load_synthetic_data():
    return {region: [] for region in REGION_NAMES}


if __name__ == '__main__':
    print(load_real_data())
    print(load_synthetic_data())
