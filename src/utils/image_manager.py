import os
import shutil

IMAGES_DIR = os.path.join('data', 'images')

def save_image(image_bytes, filename):
    """Save image bytes to the images folder."""
    os.makedirs(IMAGES_DIR, exist_ok=True)
    path = os.path.join(IMAGES_DIR, filename)
    with open(path, 'wb') as f:
        f.write(image_bytes)
    return path

def list_images():
    """List all images in the images folder."""
    os.makedirs(IMAGES_DIR, exist_ok=True)
    return [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

def delete_image(filename):
    """Delete an image from the images folder."""
    path = os.path.join(IMAGES_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
