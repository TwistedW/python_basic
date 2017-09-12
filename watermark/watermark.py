import cv2
def image_shape():
    img1 = cv2.imread("image.jpg")
    watermark_add1 = "created by wuguang"
    w1 = img1.shape[1]
    h1 = img1.shape[0]
    return img1, watermark_add1, w1, h1
def watermark_location(width, height, mark_add):
    size_watermark1 = float(input("please input your watermark size: "))
    if size_watermark1 > 1:
        w_watermark1 = int(width - len(mark_add) * 10 * size_watermark1)
        h_watermark1 = int(height - size_watermark1 * 12)
    elif 0.5 <= size_watermark1 < 1:
        w_watermark1 = int(width - len(mark_add) * 10.5 * size_watermark1)
        h_watermark1 = int(height - 12)
    else:
        w_watermark1 = int(width - len(mark_add) * 12 * size_watermark1)
        h_watermark1 = int(height - 12)
    return w_watermark1, h_watermark1, size_watermark1
def image_size_transform(img2, w2, h2):
    ResizeImg = img2
    if h2 > 700:
        ResizeImg = cv2.resize(src=img2, dsize=(int(w2*(670/h2)), 670), interpolation=cv2.INTER_LINEAR)
    elif h2 < 400:
        ResizeImg = cv2.resize(src=img2, dsize=(int(w2*(500/h2)), 500), interpolation=cv2.INTER_LINEAR)
    else:
        pass
    return ResizeImg, ResizeImg.shape[1], ResizeImg.shape[0]
if __name__ == '__main__':
    img, watermark_add, w, h, = image_shape()
    img, w, h = image_size_transform(img, w, h)
    w_watermark, h_watermark, size_watermark = watermark_location(w, h, watermark_add)
    cv2.putText(img, watermark_add, (w_watermark, h_watermark), cv2.FONT_HERSHEY_PLAIN,
                                            size_watermark, (0, 255, 0), thickness=1)
    cv2.imshow("watermark", img)
    print(img.shape)
    cv2.waitKey()
    cv2.destroyAllWindows()