import os
from configurations import *
from typing import List


def create_training_and_validation_files(baseline_folder: str, adding_synthetic_folder: str, training_images: List,
                                         validation_images: List, synthetic_images: List, num_real_training: int,
                                         num_real_validation: int, num_syn: int):
    assert os.path.isdir(baseline_folder), f'{baseline_folder} is not a directory'

    # Create paths for baseline training set
    baseline_training_imgs = open(os.path.join(baseline_folder, TRAIN_IMG_FNAME), 'w')
    baseline_training_lbls = open(os.path.join(baseline_folder, TRAIN_LBL_FNAME), 'w')
    for img in training_images[:num_real_training]:
        baseline_training_imgs.write(REAL_IMG_DIR + img + IMAGE_EXTENSION + '\n')
        baseline_training_lbls.write(REAL_LBL_DIR + img + LABEL_EXTENSION + '\n')
    baseline_training_imgs.close()
    baseline_training_lbls.close()

    # Create paths for baseline validation set
    baseline_validation_imgs = open(os.path.join(baseline_folder, VALID_IMG_FNAME), 'w')
    baseline_validation_lbls = open(os.path.join(baseline_folder, VALID_LBL_FNAME), 'w')
    for img in validation_images[:num_real_validation]:
        baseline_validation_imgs.write(REAL_IMG_DIR + img + IMAGE_EXTENSION + '\n')
        baseline_validation_lbls.write(REAL_LBL_DIR + img + LABEL_EXTENSION + '\n')
    baseline_validation_imgs.close()
    baseline_validation_lbls.close()

    if adding_synthetic_folder:
        assert os.path.isdir(adding_synthetic_folder), f'{adding_synthetic_folder} is not a directory'

        # Create paths for adding synthetic training set
        adding_synthetic_training_imgs = open(os.path.join(adding_synthetic_folder, TRAIN_IMG_FNAME), 'w')
        adding_synthetic_training_lbls = open(os.path.join(adding_synthetic_folder, TRAIN_LBL_FNAME), 'w')
        for syn_img in synthetic_images[:num_syn]:
            adding_synthetic_training_imgs.write(SYN_IMG_DIR + syn_img + IMAGE_EXTENSION + '\n')
            adding_synthetic_training_lbls.write(SYN_LBL_DIR + syn_img + LABEL_EXTENSION + '\n')
        for img in training_images[:num_real_training]:
            adding_synthetic_training_imgs.write(REAL_IMG_DIR + img + IMAGE_EXTENSION + '\n')
            adding_synthetic_training_lbls.write(REAL_LBL_DIR + img + LABEL_EXTENSION + '\n')
        adding_synthetic_training_imgs.close()
        adding_synthetic_training_lbls.close()

        # Create paths for adding synthetic validation set
        adding_synthetic_validation_imgs = open(os.path.join(adding_synthetic_folder, VALID_IMG_FNAME), 'w')
        adding_synthetic_validation_lbls = open(os.path.join(adding_synthetic_folder, VALID_LBL_FNAME), 'w')
        for img in validation_images[:num_real_validation]:
            adding_synthetic_validation_imgs.write(REAL_IMG_DIR + img + TRAIN_IMG_FNAME + '\n')
            adding_synthetic_validation_lbls.write(REAL_LBL_DIR + img + LABEL_EXTENSION + '\n')
        adding_synthetic_validation_imgs.close()
        adding_synthetic_validation_lbls.close()


def create_data_and_names_files(output_dir: str, experiment_dir: str, baseline_folder: str, adding_synthetic_folder: str):
    assert os.path.isdir(baseline_folder), f'{baseline_folder} is not a directory'

    # Create .data file for baseline folder
    with open(os.path.join(baseline_folder, BASELINE_DATA_FNAME), 'w') as baseline_data:
        baseline_data.write(f'train={output_dir}/{experiment_dir}/{BASELINE_FOLDER_NAME}/{TRAIN_IMG_FNAME}\n')
        baseline_data.write(f'train_label={output_dir}/{experiment_dir}/{BASELINE_FOLDER_NAME}/{TRAIN_LBL_FNAME}\n')
        baseline_data.write('classes=1\n')
        baseline_data.write(f'valid={output_dir}/{experiment_dir}/{BASELINE_FOLDER_NAME}/{VALID_IMG_FNAME}\n')
        baseline_data.write(f'valid_label={output_dir}/{experiment_dir}/{BASELINE_FOLDER_NAME}/{VALID_LBL_FNAME}\n')
        baseline_data.write(f'names={output_dir}/{experiment_dir}/{BASELINE_FOLDER_NAME}/{NAMES_FNAME}\n')
        baseline_data.write('backup=backup/\n')
        baseline_data.write('eval=ttx')

    # Create .names file for baseline folder
    with open(os.path.join(baseline_folder, NAMES_FNAME), 'w') as baseline_names:
        baseline_names.write('Transmission-Tower')

    if adding_synthetic_folder:
        assert os.path.isdir(adding_synthetic_folder), f'{adding_synthetic_folder} is not a directory'

        # Create .data file for adding synthetic folder
        with open(os.path.join(adding_synthetic_folder, ADDING_SYNTHETIC_DATA_FNAME), 'w') as adding_synthetic_data:
            adding_synthetic_data.write(f'train={output_dir}/{experiment_dir}/{ADDING_SYNTHETIC_FOLDER_NAME}/{TRAIN_IMG_FNAME}\n')
            adding_synthetic_data.write(f'train_label={output_dir}/{experiment_dir}/{ADDING_SYNTHETIC_FOLDER_NAME}/{TRAIN_LBL_FNAME}\n')
            adding_synthetic_data.write('classes=1\n')
            adding_synthetic_data.write(f'valid={output_dir}/{experiment_dir}/{ADDING_SYNTHETIC_FOLDER_NAME}/{VALID_IMG_FNAME}\n')
            adding_synthetic_data.write(f'valid_label={output_dir}/{experiment_dir}/{ADDING_SYNTHETIC_FOLDER_NAME}/{VALID_LBL_FNAME}\n')
            adding_synthetic_data.write(f'names={output_dir}/{experiment_dir}/{ADDING_SYNTHETIC_FOLDER_NAME}/{NAMES_FNAME}\n')
            adding_synthetic_data.write('backup=backup/\n')
            adding_synthetic_data.write('eval=ttx')

        # Create .names file for adding synthetic folder
        with open(os.path.join(adding_synthetic_folder, NAMES_FNAME), 'w') as adding_synthetic_names:
            adding_synthetic_names.write('Transmission-Tower')
