import cv2

def convert_to_grayscale(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    if image is None:
        print("Error")
        return
    
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    cv2.imwrite(output_image_path,gray_image)

    cv2.imshow("original inage", image)
    cv2.imshow("grayscale image", gray_image)

    cv2.waitKey(0)
    cv2.destoryAllWindows()

    if__name__ == "__main__":
    input_image = "input.jpg"
    output_image = "output.jpg"

    convert_to_grayscale(input_image, output_image)