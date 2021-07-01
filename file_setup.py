import os
from configurations import *


def create_data_and_names_files(output_folder, skip=[]):
    assert os.path.isdir(output_folder), f'{output_folder} is not a directory'

    baseline_folder = os.path.join(output_folder, BASELINE_FOLDER_NAME)
    adding_synthetic_folder = os.path.join(output_folder, ADDING_SYNTHETIC_FOLDER_NAME)

    # Create .data file for baseline folder
    with open(os.path.join(baseline_folder, BASELINE_DATA_FNAME), 'w') as baseline_data:
        baseline_data.write(f'train={BASELINE_FOLDER_NAME}/{TRAIN_IMG_FNAME}\n')
        baseline_data.write(f'train_label={BASELINE_FOLDER_NAME}/{TRAIN_LBL_FNAME}\n')
        baseline_data.write('classes=1\n')
        baseline_data.write(f'valid={BASELINE_FOLDER_NAME}/{VALID_IMG_FNAME}\n')
        baseline_data.write(f'valid_label={BASELINE_FOLDER_NAME}/{VALID_LBL_FNAME}\n')
        baseline_data.write(f'names={BASELINE_FOLDER_NAME}/{NAMES_FNAME}\n')
        baseline_data.write('backup=backup/\n')
        baseline_data.write('eval=wnd')

    # Create .names file for baseline folder
    with open(os.path.join(baseline_folder, NAMES_FNAME), 'w') as baseline_names:
        baseline_names.write('Transmission-Tower')

    # Create .data file for adding synthetic folder
    with open(os.path.join(adding_synthetic_folder, ADDING_SYNTHETIC_DATA_FNAME), 'w') as adding_synthetic_data:
        adding_synthetic_data.write(f'train={ADDING_SYNTHETIC_FOLDER_NAME}/{TRAIN_IMG_FNAME}\n')
        adding_synthetic_data.write(f'train_label={ADDING_SYNTHETIC_FOLDER_NAME}/{TRAIN_LBL_FNAME}\n')
        adding_synthetic_data.write('classes=1\n')
        adding_synthetic_data.write(f'valid={ADDING_SYNTHETIC_FOLDER_NAME}/{VALID_IMG_FNAME}\n')
        adding_synthetic_data.write(
            f'valid_label={ADDING_SYNTHETIC_FOLDER_NAME}/{VALID_LBL_FNAME}\n')
        adding_synthetic_data.write(f'names={ADDING_SYNTHETIC_FOLDER_NAME}/{NAMES_FNAME}\n')
        adding_synthetic_data.write('backup=backup/\n')
        adding_synthetic_data.write('eval=wnd')

    # Create .names file for adding synthetic folder
    with open(os.path.join(adding_synthetic_folder, NAMES_FNAME), 'w') as adding_synthetic_names:
        adding_synthetic_names.write('Transmission-Tower')