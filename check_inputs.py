

def check_num_images(training_images, validation_images, synthetic_images, num_real_training, num_real_validation, num_syn,
                     training_region, validation_region):
    if num_real_training == 'ALL':
        num_real_training = len(training_images)
    if num_real_validation == 'ALL':
        num_real_validation = len(validation_images)
    if num_syn == 'ALL':
        num_syn = len(synthetic_images)

    if num_real_training > len(training_images):
        print(f'Warning: There are not enough images in region {training_region} for {num_real_training} number of '
              f'real training. Found only {len(training_images)} real training images. Will use this number instead and'
              f' will update the output folder name with this number. Consider changing the ratios argument to a '
              f'smaller value')
        num_real_training = len(training_images)
    if num_real_validation > len(validation_images):
        print(f'Warning: There are not enough images in region {validation_region} for {num_real_validation} number of '
              f'real validation images. Found only {len(validation_images)} real training images. Will use this number '
              f'instead and will update the output folder name with this number. Consider changing the number of '
              f'validation images to be smaller')
        num_real_validation = len(validation_images)
    if num_syn > len(synthetic_images):
        print(f'Warning: There are not enough synthetic images in region {training_region} for {num_syn} number '
              f'of synthetic training images. Found only {len(synthetic_images)} real training images. Will use this '
              f'number instead and update the output folder name with this number. Consider changing the number of '
              f'synthetic to be smaller')
        num_syn = len(synthetic_images)

    return num_real_training, num_real_validation, num_syn
