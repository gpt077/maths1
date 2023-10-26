#program to rotate a image by 45,90,180,270 degree

def rotate(Im_1,t):
    from PIL import Image
    a1 = Image.open(IM_1)
    a1.show()
    new_a1 = a1.rotate(t)
    new_a1.show()
    new_a1.save(' path here ')

#program to crop a image
def crop(Im_1,cords):
    from PIL import Image
    a1 = Image.open(Im_1)
    a1.show()
    new_a1 = a1.crop(cords)
    new_a1.show()
    new_a1.save(' path here ')
