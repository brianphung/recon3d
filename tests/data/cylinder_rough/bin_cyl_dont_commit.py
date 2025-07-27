import glob
import tifffile
import numpy as np
import os

def binarize_tif(input_path, output_path=None, threshold=128):
    # Read the image
    img = tifffile.imread(input_path)

    # Apply threshold
    binary = (img > threshold).astype(np.uint8) * 255

    # Set output path to input path if not provided
    if output_path is None:
        output_path = input_path

    # Save the binary image
    tifffile.imwrite(output_path, binary)

for filepath in glob.glob("*.tif") + glob.glob("*.tiff"):
    binarize_tif(filepath, threshold=100)