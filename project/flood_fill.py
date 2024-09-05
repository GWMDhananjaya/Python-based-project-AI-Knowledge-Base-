"""
flood_fill.py

This module implements a flood fill algorithm for image processing using NumPy and PIL.
"""

import numpy as np
from PIL import Image

def flood_fill(image, start_x, start_y, target_color, replacement_color):
    """
    Perform a flood fill on an image.

    Args:
        image (PIL.Image): The input image to be modified.
        start_x (int): The x-coordinate of the starting pixel.
        start_y (int): The y-coordinate of the starting pixel.
        target_color (list or tuple): The color to be replaced.
        replacement_color (list or tuple): The color to replace the target color with.

    Returns:
        PIL.Image: The image with the flood fill applied.
    """
    width, height = image.size
    pixels = np.array(image)

    # Get the color of the starting pixel
    original_color = pixels[start_y, start_x]
    print(f"Starting pixel color at ({start_x}, {start_y}): {original_color}")

    # Base case: If the color is already replaced or not the target color
    if not np.array_equal(original_color, target_color):
        print("The starting pixel is not of the target color.")
        return image

    def fill(x, y):
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if np.array_equal(pixels[y, x], target_color):
            pixels[y, x] = replacement_color
            fill(x + 1, y)
            fill(x - 1, y)
            fill(x, y + 1)
            fill(x, y - 1)

    fill(start_x, start_y)
    return Image.fromarray(pixels)

# Example Usage
if __name__ == '__main__':
    try:
        # Loading and initializing variables with descriptive names
        IMAGE_PATH = "example_image.png"
        img = Image.open(IMAGE_PATH)  # Load an image
        img = img.convert("RGB")  # Ensure image is in RGB format

        fill_target_color = [255, 255, 255]  # White
        fill_replacement_color = [0, 0, 255]  # Blue
        start_pixel_x, start_pixel_y = 10, 10  # Coordinates of the pixel to start from

        result_image = flood_fill(img, start_pixel_x, start_pixel_y,
                                  fill_target_color, fill_replacement_color)

        if result_image:
            result_image.show()  # Display the modified image
            result_image.save("flood_filled_image.png")  # Save the result
        else:
            print("Flood fill did not modify the image.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error occurred: {e}")
    # Handle other potential exceptions more specifically if needed
