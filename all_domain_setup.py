import os
import argparse
from configurations import *
from file_setup import create_training_and_validation_files, create_data_and_names_files
from data import load_real_data, load_synthetic_data
from itertools import chain
from check_inputs import check_num_images
import random
from typing import Any


def main(args):
    output_dir = args.output_dir
    num_real_training = args.num_real_training_images
    num_real_validation = args.num_real_validation_images
    num_syn = args.num_synthetic_training_images
    training_region = 'ALL'
    validation_region = 'ALL'
    print(f'----- Training: {training_region} {num_real_training}, '
          f'Validating: {validation_region} {num_real_validation}, Num Syn: {num_syn} -----')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    training_images_per_region, validation_images_per_region = load_real_data()
    synthetic_images_per_region = load_synthetic_data()

    training_images = list(chain.from_iterable([images for region, images in training_images_per_region.items()]))
    validation_images = list(chain.from_iterable([images for region, images in validation_images_per_region.items()]))
    synthetic_images = list(chain.from_iterable([images for region, images in synthetic_images_per_region.items()]))

    random.shuffle(training_images)
    random.shuffle(validation_images)
    random.shuffle(synthetic_images)

    num_real_training, num_real_validation, num_syn = check_num_images(training_images=training_images,
                                                                       validation_images=validation_images,
                                                                       synthetic_images=synthetic_images,
                                                                       num_real_training=num_real_training,
                                                                       num_real_validation=num_real_validation,
                                                                       num_syn=num_syn,
                                                                       training_region=training_region,
                                                                       validation_region=validation_region)

    output_folder = os.path.join(output_dir, f'Train-{training_region}-{num_real_training}-'
                                             f'Val-{validation_region}-{num_real_validation}-Syn-{num_syn}')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Create folders for the baseline and adding_synthetic data for the current pair of regions
    baseline_folder = os.path.join(output_folder, BASELINE_FOLDER_NAME)
    if not os.path.exists(baseline_folder):
        os.mkdir(baseline_folder)

    adding_synthetic_folder = os.path.join(output_folder, ADDING_SYNTHETIC_FOLDER_NAME)
    if not os.path.exists(adding_synthetic_folder):
        os.mkdir(adding_synthetic_folder)

    create_data_and_names_files(baseline_folder=baseline_folder,
                                adding_synthetic_folder=adding_synthetic_folder)

    create_training_and_validation_files(baseline_folder=baseline_folder,
                                         adding_synthetic_folder=adding_synthetic_folder,
                                         training_images=training_images,
                                         validation_images=validation_images,
                                         synthetic_images=synthetic_images,
                                         num_real_training=num_real_training,
                                         num_real_validation=num_real_validation,
                                         num_syn=num_syn)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', type=str, default=DEFAULT_OUTPUT_DIR,
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-t', '--num-real-training-images', default='ALL',
                        help='Number of real training images to use. "ALL" to use all images, otherwise use int')
    parser.add_argument('-v', '--num-real-validation-images', default='ALL',
                        help='Number of real validation images to use. "ALL" to use all images, otherwise use int')
    parser.add_argument('-s', '--num-synthetic-training-images', default='ALL',
                        help='Number of synthetic training images to use. "ALL" to use all images, otherwise use int')
    args = parser.parse_args()
    main(args)
