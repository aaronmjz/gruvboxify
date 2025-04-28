import sys
import numpy as np
from PIL import Image
import argparse

GRUVBOX_DARK_PALETTE = [
    (40, 40, 40),    # bg0
    (60, 56, 54),    # bg1
    (80, 73, 69),    # bg2
    (102, 92, 84),   # bg3
    (124, 111, 100), # bg4
    (146, 131, 116), # fg0
    (168, 153, 132), # fg1
    (213, 196, 161), # fg2
    (235, 219, 178), # fg3
    (251, 241, 199), # fg4
    (251, 73, 52),   # red
    (184, 187, 38),  # yellow
    (250, 189, 47),  # orange
    (131, 165, 152), # aqua
    (142, 192, 124), # green
    (211, 134, 155), # pink
    (214, 93, 14),   # bright orange
    (152, 151, 26),  # bright yellow
    (184, 187, 38),  # bright yellow2
    (104, 157, 106), # bright green
    (69, 133, 136),  # blue
    (177, 98, 134),  # purple
    (214, 93, 14),   # bright orange2
]

def convert_image_to_gruvbox(input_path, output_path):
    img = Image.open(input_path).convert('RGB')
    data = np.array(img)
    shape = data.shape
    flat_data = data.reshape(-1, 3)
    palette = np.array(GRUVBOX_DARK_PALETTE)
    dists = np.sum((flat_data[:, None, :] - palette[None, :, :]) ** 2, axis=2)
    nearest = np.argmin(dists, axis=1)
    new_flat = palette[nearest]
    new_data = new_flat.reshape(shape)
    new_img = Image.fromarray(new_data.astype('uint8'), 'RGB')
    new_img.save(output_path)
    print(f"Saved Gruvbox palette image to {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert any image to the Gruvbox color palette."
    )
    parser.add_argument('input_image', nargs='?', help='Path to the input image file')
    parser.add_argument('output_image', nargs='?', help='Path to save the Gruvboxified image')
    args = parser.parse_args()

    if not args.input_image or not args.output_image:
        parser.print_help()
        sys.exit(1)

    convert_image_to_gruvbox(args.input_image, args.output_image) 
