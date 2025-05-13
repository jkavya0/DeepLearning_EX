from tmp import ImageGenerator

# Use raw string (r"") to avoid Windows path errors with backslashes
file_path = r"C:\Users\jkavy\DeepLearning\exercise0\src_to_implement\data\reference_arrays"
label_path = r"C:\Users\jkavy\DeepLearning\exercise0\src_to_implement\data\labels.json"

# Batch size and image size: [height, width, channels]
batch_size = 9
image_size = [64, 64, 3]  # Adjust depending on your input images

# Create generator object
gen = ImageGenerator(
    file_path=file_path,
    label_path=label_path,
    batch_size=batch_size,
    image_size=image_size,
    rotation=True,
    mirroring=True,
    shuffle=True
)

# Visualize one batch
gen.show()

# Optionally, print one batch as arrays:
# images, labels = gen.next()
# print(images.shape)
# print(labels)
