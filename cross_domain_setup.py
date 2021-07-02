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

    for ratio in ratios:
        for i in range(len(region_pairs)):

            num_real, num_syn = ratio
            pair_names = region_pairs[i]
            training_region, validation_region = pair_names
            print(f'----- Training {training_region}, Validating {validation_region}, '
                  f'Num Real: {num_real} Num Syn: {num_syn} -----')

            training_images, validation_images = training_images_per_region[training_region].copy(), \
                                                 validation_images_per_region[validation_region].copy()

            synthetic_images = synthetic_images_per_region[validation_region].copy()

            random.shuffle(training_images)
            random.shuffle(validation_images)
            random.shuffle(synthetic_images)

            # Compare num_real and num_syn input from the user with how many images we actually have and give a warning
            # if we don't have enough
            if num_real > len(training_images):
                print(f'Warning: There are not enough images in region {training_region} for {num_real} number of '
                      f'real training images. Will use {len(training_images)} real training images instead. '
                      f'Consider changing the ratios argument to a smaller value')
            if num_real > len(validation_images):
                print(f'Warning: There are not enough images in region {validation_region} for {num_real} number of '
                      f'real validation images. Will use {len(validation_images)} validation images instead. '
                      f'Consider changing the ratios argument to a smaller value')
            if num_syn > len(synthetic_images):
                print(f'Warning: There are not enough synthetic images in region {training_region} for {num_syn} number '
                      f'of synthetic training images. Will use {len(synthetic_images)} synthetic training images instead. '
                      f'Consider changing the ratios argument to a smaller value')

            # Create the folder for the current pair of regions
            output_folder = os.path.join(output_dir,
                                         f'Train-{training_region}-Val-{validation_region}-{str(num_real)}-real-{str(num_syn)}-syn')
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

            # Create .txt files for image and label paths for baseline and adding synthetic
            create_training_and_validation_files(baseline_folder=baseline_folder,
                                                 adding_synthetic_folder=adding_synthetic_folder,
                                                 training_images=training_images,
                                                 validation_images=validation_images,
                                                 synthetic_images=synthetic_images,
                                                 num_real=num_real,
                                                 num_syn=num_syn)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, default=DEFAULT_OUTPUT_DIR,
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-r', '--ratios', type=List[List[int]], default=DEFAULT_RATIOS,
                        help='Nested list with number of real images followed by number of synthetic images. See '
                             'configurations.py')
    parser.add_argument('-p', '--region-pairs', type=List[List[str]], default=DEFAULT_REGION_PAIRS,
                        help='Pairs of regions to setup experiments for. See configurations.py')
    args = parser.parse_args()
    main(args)
