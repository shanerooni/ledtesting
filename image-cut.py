#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image, ImageOps, ImageFont
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions


class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open('/home/pi/rpi-rgb-led-matrix/img/logo.png').convert('RGB') #Image.open(self.args.image).convert('RGB')
        self.image.resize((256, 96), Image.ANTIALIAS) #self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

	# RGB example w/graphics prims.
	# Note, only "RGB" mode is supported currently.
	image = Image.new("RGB", (256, 96))  # Can be larger than matrix if wanted!!
	#draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
	# Draw some shapes into image (no immediate effect on matrix)...
	#draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0), outline=(0, 0, 255))
	#draw.line((0, 0, 31, 31), fill=(255, 0, 0))
	#draw.line((0, 31, 31, 0), fill=(0, 255, 0))

	

	img1 = Image.open('/home/pi/rpi-rgb-led-matrix/img/logo.png')
	size = (256, 96)
	img = ImageOps.fit(img1, size, Image.ANTIALIAS)
	fnt = ImageFont.truetype('/home/pi/rpi-rgb-led-matrix/fonts/digital2.ttf', 100)
	d = ImageDraw.Draw(img)
	d.text((0,0), "02:34",font=fnt, fill=(255,255,255))
	#sub_image1 = img.crop(box=(0,0,255,31)).rotate(180)
	#sub_image2 = img.crop(box=(0,32,255,64))
	sub_image1 = img.crop(box=(0,0,255,95))
	#sub_image3 = img.crop(box=(0,64,255,96)).rotate(180)
	#image.paste(sub_image1, box=(0,0))
	#image.paste(sub_image2, box=(257,0))
	#image.paste(sub_image3, box=(512,0))
	image.paste(sub_image1, box=(0,0))
	##image.save('/home/pi/rpi-rgb-led-matrix/img/logo12.png')
	self.image = image

        double_buffer = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size

        # let's scroll
        xpos = 0
        while True:
            xpos += 0 #1
            if (xpos > img_width):
                xpos = 0

            double_buffer.SetImage(self.image, -xpos)
            double_buffer.SetImage(self.image, -xpos + img_width)

            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            time.sleep(5) #(0.01)

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
