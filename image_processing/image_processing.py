import cv2
if __name__ == '__main__':
    img = cv2.imread("image1.jpg")
    w = img.shape[1]
    h = img.shape[0]
    for xi in range(0, w):
        for xj in range(0,h):
            img[xj, xi, 0] = int(img[xj, xi, 0]*0.7)
            img[xj, xi, 1] = int(img[xj, xi, 1] * 0.7)
        if xi % 1000 == 0:
            print('.')
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.imwrite("image2.jpg",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
