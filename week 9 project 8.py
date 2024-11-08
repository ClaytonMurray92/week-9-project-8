from image import Images
def grayscale(image):
    width, height = image.size
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels[x, y] = (gray, gray, gray)
        return image
def sepia(image):
    image = grayscale(image)
    width, height = image.size
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            pixels[x, y] = (r, g, b)
        return image
if __name__ == "__main__":
    image_path = "image.gif"
    image = Image.open(image_path)
