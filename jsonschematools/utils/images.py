import base64
import io
from io import BytesIO

from PIL.Image import Image


def im_2_b64(image: Image, format: str = "JPEG") -> str:
    buff = BytesIO()
    image.save(buff, format=format)
    img_str = base64.b64encode(buff.getvalue()).decode("utf-8")
    return img_str

