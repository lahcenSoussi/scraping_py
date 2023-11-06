import fitz
import PIL.Image
import os
import io

file = fitz.open("file.pdf")
counter = 1
for page_index in range(len(file)):
    page = file[page_index]
    images = page.get_images()
    for image in images:
        try:
            base_img = file.extract_image(image[0])
            img_dt = base_img["image"]
            image_name = PIL.Image.open(io.BytesIO(img_dt))
            ext = base_img['ext']
            image_name.save(open(f"img{counter}.{ext}","wb"))
            counter += 1
        except Exception as e:
            print(e)
            

