from PIL import Image, ImageFilter,ImageEnhance
import io, pytesseract, requests,urllib3,re
urllib3.disable_warnings()
response = requests.get(url_captcha,verify=False)
with open('captcha.png','wb') as f:
    f.write(response.content)
im =  Image.open('captcha.png')
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
text = pytesseract.image_to_string(im,lang='eng')
