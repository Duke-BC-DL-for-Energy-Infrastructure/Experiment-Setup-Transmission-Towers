import os
from configurations import *
from typing import Dict, List
import csv
import glob


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


def load_synthetic_data() -> Dict[str, List[str]]:
    """
    :return:
    Will return a dictionary in format {'region' : [list of synthetic images in region]}
    e.g. {'SW': [Arizona_id_302392_459, Arizona_id_306003_515, ...], 'NE': [Pennsylvania_id_129442_57, ...], ...}
    """

    synthetic_data = {region: [] for region in REGION_NAMES}
    if not os.path.exists(SYNTHETIC_CSV_PATH):
        print(f'Did not find csv file at {SYNTHETIC_CSV_PATH}, given by SYNTHETIC_CSV_PATH in configurations.py. '
              f'Will return empty dictionary for synthetic images')
        return synthetic_data

    with open(SYNTHETIC_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        for idx, row in enumerate(csvreader):
            region = row[0]
            filename = row[1]
            synthetic_data[region].append(filename)
    return synthetic_data


def collect_syn_data(syn_dir):
    """
    :param syn_dir: path to the directory where the synthetic data is stored. Assumes that the directory is organized
    such that there is a folder named with the region name. Following is an example of a directory structure where
    we have all four regions.

    - > syn_dir
        - > EM
            - > color_all_images_step608
                - > image1.png
                - > image2.png
        - > NE
        - > NW
        - > SW

    Here, color_all_images_step608 is specified in configurations.py and is the name of the directory that CityEngine
    creates for the images that it generates

    Creates a csv file with the same name as SYNTHETIC_CSV_PATH, where there is a field for region and for filename.
    This file is then used by load_synthetic_data
    """
    with open(SYNTHETIC_CSV_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["region", "filename"])
        for region in REGION_NAMES:
            region_dir_path = os.path.join(syn_dir, region, CITYENGINE_IMAGE_DIRECTORY_NAME)
            if os.path.exists(region_dir_path):
                print(f'Found directory for {region}')
                paths = glob.glob(os.path.join(region_dir_path, f'*{SYN_IMAGE_EXTENSION}'))
                for path in paths:
                    basename = os.path.basename(path)
                    filename = os.path.splitext(basename)[0]
                    writer.writerow([region, filename])
            else:
                pass
    return


if __name__ == '__main__':
    print(load_real_data())
    print(load_synthetic_data())
    #collect_syn_data(SYN_DIR)
