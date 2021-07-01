import os
import argparse
from configurations import *
from data import load_data
from file_setup import create_data_and_names_files
import random


def main(args):
    output_dir = args.output_dir
    ratios = args.ratios
    region_pairs = args.region_pairs

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    training_images, validation_images = load_data()

    # CREATE OUTPUTS:
    for ratio in ratios:
        for i in range(len(region_pairs)):
            pair_names = region_pairs[i]
            pair_trn_images, pair_val_images = training_images[pair_names[0]].copy(), \
                                               validation_images[pair_names[1]].copy()
            random.shuffle(pair_trn_images)
            random.shuffle(pair_val_images)
            pair_images = [pair_trn_images, pair_val_images]

            # Create the folder for the current pair of regions
            output_folder = os.path.join(output_dir,
                                         f'Train-{pair_names[0]}-Val-{pair_names[1]}-{str(ratio[0])}-real-{str(ratio[1])}-syn')
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
            create_data_and_names_files(output_folder=output_folder)

            # Create paths for baseline training set
            baseline_training_imgs = open(os.path.join(baseline_folder, TRAIN_IMG_FNAME), 'w')
            baseline_training_lbls = open(os.path.join(baseline_folder, TRAIN_LBL_FNAME), 'w')
            for img in pair_images[0][:ratio[0]]:
                baseline_training_imgs.write(REAL_IMG_DIR + img + IMAGE_EXTENSION + '\n')
                baseline_training_lbls.write(REAL_LBL_DIR + img + LABEL_EXTENSION + '\n')
            baseline_training_imgs.close()
            baseline_training_lbls.close()

            # Create paths for baseline validation set
            baseline_validation_imgs = open(os.path.join(baseline_folder, VALID_IMG_FNAME), 'w')
            baseline_validation_lbls = open(os.path.join(baseline_folder, VALID_LBL_FNAME), 'w')
            for img in pair_images[1][:ratio[0]]:
                baseline_validation_imgs.write(REAL_IMG_DIR + img + IMAGE_EXTENSION + '\n')
                baseline_validation_lbls.write(REAL_LBL_DIR + img + LABEL_EXTENSION + '\n')
            baseline_validation_imgs.close()
            baseline_validation_lbls.close()

            # # Create paths for adding synthetic training set
            # adding_synthetic_training_imgs = open(os.path.join(adding_synthetic_folder, training_img_txt_filename), 'w')
            # adding_synthetic_training_lbls = open(os.path.join(adding_synthetic_folder, training_lbl_txt_filename), 'w')
            # for img in syn_data[i][:ratio[1]]:
            #     adding_synthetic_training_imgs.write('../data/synthetic_images/' + img.split(separator)[-1] + '\n')
            #     adding_synthetic_training_lbls.write(
            #         '../data/synthetic_labels/' + img.split(separator)[-1].replace('.png', '.txt') + '\n')
            # for img in pair_images[0][:ratio[0]]:
            #     adding_synthetic_training_imgs.write('../data/images/' + img + '.jpg' + '\n')
            #     adding_synthetic_training_lbls.write('../data/labels/' + img + '.txt' + '\n')
            # adding_synthetic_training_imgs.close()
            # adding_synthetic_training_lbls.close()
            #
            # # Create paths for adding synthetic validation set
            # adding_synthetic_validation_imgs = open(os.path.join(adding_synthetic_folder, validation_img_txt_filename),
            #                                         'w')
            # adding_synthetic_validation_lbls = open(os.path.join(adding_synthetic_folder, validation_lbl_txt_filename),
            #                                         'w')
            # for img in pair_images[1][:ratio[0]]:
            #     adding_synthetic_validation_imgs.write('../data/images/' + img + '.jpg' + '\n')
            #     adding_synthetic_validation_lbls.write('../data/labels/' + img + '.txt' + '\n')
            # adding_synthetic_validation_imgs.close()
            # adding_synthetic_validation_lbls.close()

    return


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
