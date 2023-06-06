from PIL import Image
import os


def crop_image_by_bbox(image_path, bbox):
    try:
        # Load the image
        image = Image.open(image_path)

        # Check if the bounding box exceeds image boundaries
        if bbox[0] < 0 or bbox[1] < 0:
            raise ValueError("Bounding box exceeds image boundaries.")

        # Crop the image based on the bounding box coordinates
        cropped_image = image.crop(bbox)

        return cropped_image
    except Exception as e:
        print(f"Error cropping image {image_path}: {str(e)}")
        return None


def crop_images_by_bboxes(image_paths, bounding_boxes):
    # Create a directory to store the cropped images
    output_dir = "cropped_images"
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each image and its corresponding bounding box
    for i, (image_path, bbox) in enumerate(zip(image_paths, bounding_boxes)):
        # Crop the image
        cropped_image = crop_image_by_bbox(image_path, bbox)

        if cropped_image:
            # Generate the output filename
            filename = os.path.splitext(os.path.basename(image_path))[0]
            output_filename = f"cropped_image_{filename}_{i}.jpg"

            # Save the cropped image
            cropped_image.save(os.path.join(output_dir, output_filename))
            print(f"Cropped image saved: {output_filename}")


# Example usage
image_paths = ['F:\shifat.png', 'F:\shi.png']
bounding_boxes = [
    (813, 133, 1279, 697),  # Bounding box for image1.jpg
    (812, 126, 1278, 690)   # Bounding box for image2.png
]

crop_images_by_bboxes(image_paths, bounding_boxes)
