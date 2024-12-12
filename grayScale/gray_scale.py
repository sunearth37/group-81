import cv2
import os

def convert_to_grayscale(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    if image is None:
        print("Error: Unable to load the image.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output_image_path, gray_image)

    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image = "C:\\Users\\82109\\Downloads\\input.jpg"

    # Set output path to the Downloads folder
    downloads_folder = os.path.expanduser("C:\\Users\\82109\\Downloads\\")
    output_image = os.path.join(downloads_folder, "output.jpg")

    convert_to_grayscale(input_image, output_image)
