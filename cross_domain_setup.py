import os
import glob
import argparse
from typing import List, Tuple
from configurations import *
from data import load_data
from file_setup import create_data_and_names_files


def main(args):
    output_dir = args.output_dir
    ratios = args.ratios
    region_pairs = args.region_pairs

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

            # Create .data and .names files
            create_data_and_names_files(output_folder=output_folder)

            # Create folders for the baseline and adding_synthetic data for the current pair of regions
            baseline_folder = os.path.join(output_folder, BASELINE_FOLDER_NAME)
            if not os.path.exists(baseline_folder):
                os.mkdir(baseline_folder)

            adding_synthetic_folder = os.path.join(output_folder, ADDING_SYNTHETIC_FOLDER_NAME)
            if not os.path.exists(adding_synthetic_folder):
                os.mkdir(adding_synthetic_folder)

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, default='output',
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-r', '--ratios', type=List[List[int]], default=DEFAULT_RATIOS,
                        help='Tuple with number of real images followed by number of synthetic images')
    parser.add_argument('-p', '--region-pairs', type=List[List[str]], default=DEFAULT_REGION_PAIRS,
                        help='Pairs of regions to setup experiments for')
    args = parser.parse_args()
    main(args)
