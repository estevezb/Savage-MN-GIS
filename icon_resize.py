from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width}x{height}")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width}x{height}")
    resized_image.show()
    resized_image.save(output_image_path)

resize_image('content/images/favicon-500x500.png', 'content/images/favicon-48x48.png', (48, 48))