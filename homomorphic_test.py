import cv2
import os
import homofilt
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# 설치한 tesseract 프로그램 경로 (64비트)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# 이미지 불러오기
image = cv2.imread("menu4.jpg")
#Gray 프로세싱
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#바이너리 처리
binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1];

#homomorphic filter
homo_filter = homofilt.HomomorphicFilter(a = 0.75, b = 1.25)
filtimg = homo_filter.filter(I=binary, filter_params=[30,2])


# write the grayscale image to disk as a temporary file so we can
# 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장.
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, filtimg)

# Simple image to string
text = pytesseract.image_to_string(Image.open(filename), lang='kor')
#os.remove(filename)

print(text)
