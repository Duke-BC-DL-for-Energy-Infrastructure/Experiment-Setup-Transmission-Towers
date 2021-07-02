import os
import argparse
from configurations import *
from data import load_real_data, load_synthetic_data
from file_setup import create_data_and_names_files, create_training_and_validation_files
import random


def main(args):
    output_dir = args.output_dir
    ratios = args.ratios
    region_pairs = args.region_pairs

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    training_images_per_region, validation_images_per_region = load_real_data()
    synthetic_images_per_region = load_synthetic_data()

    # CREATE OUTPUTS:
    for ratio in ratios:
        for i in range(len(region_pairs)):
            pair_names = region_pairs[i]
            training_region, validation_region = pair_names
            train_images, validation_images = training_images_per_region[training_region].copy(), \
                                              validation_images_per_region[validation_region].copy()
            random.shuffle(train_images)
            random.shuffle(validation_images)

            synthetic_images = synthetic_images_per_region[validation_region]

            # Create the folder for the current pair of regions
            output_folder = os.path.join(output_dir, f'Train-{pair_names[0]}-Val-{pair_names[1]}-{str(ratio[0])}-real-{str(ratio[1])}-syn')
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)

            # Create folders for the baseline and adding_synthetic data for the current pair of regions
            baseline_folder = os.path.join(output_folder, BASELINE_FOLDER_NAME)
            if not os.path.exists(baseline_folder):
                os.mkdir(baseline_folder)

            adding_synthetic_folder = os.path.join(output_folder, ADDING_SYNTHETIC_FOLDER_NAME)
            if not os.path.exists(adding_synthetic_folder):
                os.mkdir(adding_synthetic_folder)

            # Create .data and .names files
            create_data_and_names_files(baseline_folder=baseline_folder,
                                        adding_synthetic_folder=adding_synthetic_folder)

            create_training_and_validation_files(baseline_folder=baseline_folder,
                                                 adding_synthetic_folder=adding_synthetic_folder,
                                                 train_images=train_images,
                                                 validation_images=validation_images,
                                                 synthetic_images=synthetic_images,
                                                 ratio=ratio)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, default='output',
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-r', '--ratios', type=List[List[int]], default=DEFAULT_RATIOS,
                        help='Nested list with number of real images followed by number of synthetic images. See '
                             'configurations.py')
    parser.add_argument('-p', '--region-pairs', type=List[List[str]], default=DEFAULT_REGION_PAIRS,
                        help='Pairs of regions to setup experiments for. See configurations.py')
    args = parser.parse_args()
    main(args)
