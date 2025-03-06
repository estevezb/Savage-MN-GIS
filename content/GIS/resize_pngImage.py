from PIL import Image


# Increase the maximum allowed image size
Image.MAX_IMAGE_PIXELS = None  # Disables the decompression bomb limit

input_path = r"C:\Projects\my_git_pages_website\Py-and-Sky-Labs\content\images\Dominica2017_RGB_Extracted.png"
output_path = r"C:\Projects\my_git_pages_website\Py-and-Sky-Labs\content\images\Dominica2017_RGB_Extracted_resized.png"


img = Image.open(input_path)
img= img.resize((1200,800)) # Resize to smaller size more manageable size for web display
img.save(output_path)

print("Resized image saved",output_path)