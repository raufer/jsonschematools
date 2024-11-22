from PIL import Image

from pathlib import Path
from .images import im_2_b64


def encode_image_from_file(filepath: str, format: str = "JPEG") -> str:
    """Encodes an image from a file and returns a base64 string"""
    extension = Path(filepath).suffix.upper()
    image = Image.open(filepath)

    if extension == '.PNG':
        format = 'PNG'
    elif extension in ['.JPG', '.JPEG']:
        format = 'JPEG'
    else:
        raise ValueError(f"Unsupported image format: {extension}")

    return im_2_b64(image, format=format)
