import cv2 as cv


def resize(img, scale=0.75):
    width = int(img.shape[0] * scale)
    height = int(img.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("photos/CAT.jpeg")
resized_img = resize(img, 10)

cv.imshow('cat', resized_img)

cv.waitKey(0)
