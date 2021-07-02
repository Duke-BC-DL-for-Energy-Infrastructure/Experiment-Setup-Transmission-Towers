import os
import argparse
from configurations import *
from file_setup import create_training_and_validation_files, create_data_and_names_files
from data import load_real_data, load_synthetic_data
from itertools import chain
import random


def main(args):
    val_size = args.val_size
    output_dir = args.output_dir
    fraction_of_data_to_use = args.fraction_of_data_to_use

    assert 0 < val_size < 1.0, f'val-size: {val_size}, is not a valid size for the validation set. ' \
                               f'Should be between 0 and 1'
    assert 0 < fraction_of_data_to_use < 1.0 f'fraction-of-data-to-use: {fraction_of_data_to_use}, is not a valid' \
                                             f'fraction. Should be between 0 and 1'

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    training_images_per_region, validation_images_per_region = load_real_data()
    synthetic_images_per_region = load_synthetic_data()

    training_images = list(chain.from_iterable([images for region, images in training_images_per_region.items()]))
    validation_images = list(chain.from_iterable([images for region, images in validation_images_per_region.items()]))
    real_images = training_images + validation_images

    synthetic_images = list(chain.from_iterable([images for region, images in synthetic_images_per_region.items()]))

    random.shuffle(real_images)
    random.shuffle(synthetic_images)

    # TODO get num_real and num_syn based on the arguments that control training and validation dataset size
    output_folder = os.path.join(output_dir,
                                 f'All-Domains-TrainReal-{num_real_training}-ValReal-{num_real_validation}-{num_syn}-syn')
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

    # TODO fill in arguments to create_training_and_validation_files
    create_training_and_validation_files(baseline_folder=baseline_folder,
                                         adding_synthetic_folder=adding_synthetic_folder,
                                         training_images=,
                                         validation_images=,
                                         synthetic_images=,
                                         num_real_training=,
                                         num_real_validation=,
                                         num_syn=)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # TODO decide on what arguments to use for controlling size of train and validation set and number of synthetic
    parser.add_argument('-o', '--output-dir', type=str, default=DEFAULT_OUTPUT_DIR,
                        help='Path to directory where files/directories will be generated')
    parser.add_argument('-v', '--val-size', type=float, default=0.1,
                        help='Proportion of data that goes into the validation set')
    parser.add_argument('-f', '--fraction-of-data-to-use', type=float, default=1.0,
                        help='The fraction of the total data to use. To use all data, this should be 1.0')
    args = parser.parse_args()
    main(args)