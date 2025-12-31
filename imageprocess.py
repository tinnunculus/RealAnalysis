import cv2
import numpy as np
import os

def resize_image(image, width=None, height=None):
    """Resize an image to the given width and height while maintaining aspect ratio."""
    if width is None and height is None:
        return image

    (h, w) = image.shape[:2]
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
    return resized

if __name__ == "__main__":
    # Example usage
    img = cv2.imread(os.path.join("Intro_RA", "ch6", "6_2_4.jpeg"))
    # img = resize_image(img, width=768)
    cv2.imwrite('resized_example.png', img)