import os
import glob
import argparse
from typing import List, Tuple
from configurations import *


def main(args):
    output_dir = args.output_dir
    ratios = args.ratios
    region_pairs = args.region_pairs

    load_data()

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # CREATE OUTPUTS:
    for ratio in ratios:
        for i in range(len(region_pairs)):
            pair_names = region_pairs[i]
            pair = pairs[i] # TODO Need this changed to be the image names per region

            # Create the folder for the current pair of regions
            output_folder = os.path.join(output_dir,
                                         f'Train {pair_names[0]} Val {pair_names[1]} {str(ratio[0])} real {str(ratio[1])} syn')
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)

            # Create folders for the baseline and adding_synthetic data for the current pair of regions
            baseline_folder = os.path.join(output_folder, BASELINE_FOLDER_NAME)
            if not os.path.exists(baseline_folder):
                os.mkdir(baseline_folder)

            adding_synthetic_folder = os.path.join(output_folder, ADDING_SYNTHETIC_FOLDER_NAME)
            if not os.path.exists(adding_synthetic_folder):
                os.mkdir(adding_synthetic_folder)

            # Create .data file for baseline folder
            with open(os.path.join(baseline_folder, BASELINE_DATA_FNAME), 'w') as baseline_data:
                baseline_data.write(f'train={BASELINE_FOLDER_NAME}/{TRAIN_IMG_FNAME}\n')
                baseline_data.write(f'train_label={BASELINE_FOLDER_NAME}/{TRAIN_LBL_FNAME}\n')
                baseline_data.write('classes=1\n')
                baseline_data.write(f'valid={BASELINE_FOLDER_NAME}/{VALID_IMG_FNAME}\n')
                baseline_data.write(f'valid_label={BASELINE_FOLDER_NAME}/{VALID_LBL_FNAME}\n')
                baseline_data.write(f'names={BASELINE_FOLDER_NAME}/ttw.names\n')
                baseline_data.write('backup=backup/\n')
                baseline_data.write('eval=wnd')

            # # Create .data file for adding synthetic folder
            # with open(os.path.join(adding_synthetic_folder, ADDING_SYNTHETIC_DATA_FNAME),
            #           'w') as adding_synthetic_data:
            #     adding_synthetic_data.write(f'train={ADDING_SYNTHETIC_FOLDER_NAME}/{TRAIN_IMG_FNAME}\n')
            #     adding_synthetic_data.write(f'train_label={ADDING_SYNTHETIC_FOLDER_NAME}/{TRAIN_LBL_FNAME}\n')
            #     adding_synthetic_data.write('classes=1\n')
            #     adding_synthetic_data.write(f'valid={ADDING_SYNTHETIC_FOLDER_NAME}/{VALID_IMG_FNAME}\n')
            #     adding_synthetic_data.write(
            #         f'valid_label={ADDING_SYNTHETIC_FOLDER_NAME}/{VALID_LBL_FNAME}\n')
            #     adding_synthetic_data.write(f'names={ADDING_SYNTHETIC_FOLDER_NAME}/wnd.names\n')
            #     adding_synthetic_data.write('backup=backup/\n')
            #     adding_synthetic_data.write('eval=wnd')

            # Create .names file for baseline folder
            with open(os.path.join(BASELINE_FOLDER_NAME, 'wnd.names'), 'w') as baseline_names:
                baseline_names.write('Transmission-Tower')

            # # Create .names file for adding synthetic folder
            # with open(os.path.join(ADDING_SYNTHETIC_FOLDER_NAME, 'wnd.names'), 'w') as adding_synthetic_names:
            #     adding_synthetic_names.write('Transmission-Tower')

            # Create paths for baseline training set
            baseline_training_imgs = open(os.path.join(baseline_folder, TRAIN_IMG_FNAME), 'w')
            baseline_training_lbls = open(os.path.join(baseline_folder, TRAIN_LBL_FNAME), 'w')
            for img in pair[0][:ratio[0]]:
                baseline_training_imgs.write('../data/images/' + img + '.jpg' + '\n')
                baseline_training_lbls.write('../data/labels/' + img + '.txt' + '\n')
            baseline_training_imgs.close()
            baseline_training_lbls.close()

            # Create paths for baseline validation set
            baseline_validation_imgs = open(os.path.join(baseline_folder, VALID_IMG_FNAME), 'w')
            baseline_validation_lbls = open(os.path.join(baseline_folder, VALID_LBL_FNAME), 'w')
            for img in pair[1][:ratio[0]]:
                baseline_validation_imgs.write('../data/images/' + img + '.jpg' + '\n')
                baseline_validation_lbls.write('../data/labels/' + img + '.txt' + '\n')
            baseline_validation_imgs.close()
            baseline_validation_lbls.close()

    return


def load_data():
    assert os.path.isfile(TRAIN_CSV_PATH), f'TRAIN_CSV_PATH: {TRAIN_CSV_PATH} is not a valid file'
    assert os.path.isfile(TEST_CSV_PATH), f'TEST_CSV_PATH: {TEST_CSV_PATH} is not a valid file'
    assert os.path.isfile(IMAGES_TO_IGNORE_PATH), f'IMAGES_TO_IGNORE_PATH: {IMAGES_TO_IGNORE_PATH} is not a valid file'

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, default='output',
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-r', '--ratios', type=List[List[int, int]], default=DEFAULT_RATIOS,
                        help='Tuple with number of real images followed by number of synthetic images')
    parser.add_argument('-p', '--region-pairs', type=List[List[str, str]], default=DEFAULT_REGION_PAIRS,
                        help='Pairs of regions to setup experiments for')
    args = parser.parse_args()
    main(args)
