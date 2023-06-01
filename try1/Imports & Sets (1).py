
# Load the image
img = imread('Downloads\\dolphin.png')

# Display the original image
imshow('Original Image', img)
waitKey(0)

# Crop the image
cropped = img[110:310, 10:160]

# Display the cropped image
imshow('Cropped Image', cropped)
waitKey(0)

# Find the size of the cropped image
cropped_height, cropped_width, _ = cropped.shape
print('Cropped image size:', cropped_width, 'x', cropped_height)
destroyAllWindows()

