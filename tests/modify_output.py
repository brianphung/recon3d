import glob
import tifffile
import numpy as np
import os

def binarize_tif(input_path, output_path):
    # Read the image
    img = tifffile.imread(input_path)

    # Map values: 1 → 255, 2 → 0, 3 → 126
    mapping = {1: 255, 2: 0, 3: 126}
    binary = np.zeros_like(img, dtype=np.uint8)
    for orig, new in mapping.items():
        binary[img == orig] = new

    # Save the mapped image
    tifffile.imwrite(output_path, binary)

# Define input and output directories
input_dir = '/Users/brian/Work/projects/recon3d/tests/data/output/binary_to_semantic'    # Replace with your actual input folder
output_dir = '/Users/brian/Work/projects/recon3d/tests/data/output/viz_images'  # Replace with your actual output folder

os.makedirs(output_dir, exist_ok=True)

# Process all .tif and .tiff files
for filepath in glob.glob(os.path.join(input_dir, '*.tif')) + glob.glob(os.path.join(input_dir, '*.tiff')):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_modified{ext}")
    binarize_tif(filepath, output_path)