from PIL import Image, ImageFilter, ImageOps

def apply_filter(img: Image.Image, name: str) -> Image.Image:
    name = name.lower()
    if name == "gray":
        return ImageOps.grayscale(img).convert("RGB")
    if name == "sepia":
        g = ImageOps.grayscale(img)
        return Image.merge("RGB", (
            g.point(lambda p: int(p * 1.07)),
            g.point(lambda p: int(p * 0.74)),
            g.point(lambda p: int(p * 0.43)),
        ))
    if name == "blur":
        return img.filter(ImageFilter.GaussianBlur(radius=3))
    if name == "edge":
        return img.filter(ImageFilter.FIND_EDGES)
    if name == "poster":
        return ImageOps.posterize(img.convert("RGB"), bits=3)
    if name == "solar":
        return ImageOps.solarize(img, threshold=128)
    return img