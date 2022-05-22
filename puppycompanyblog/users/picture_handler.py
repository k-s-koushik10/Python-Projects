from PIL import Image
import os
from flask import url_for, current_app

def add_profile_pic(pic_upload,username):

    filename = pic_upload.filename #mypic.jpg
    ext_type = filename.split('.')[-1] #mypic . jpg --> jpg = [-1]
    storage_filename = str(username)+'.'+ext_type #username.jpg
    file_path = os.path.join(current_app.root_path,'static\profile_pics',storage_filename)

    output_size = (250,250)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(file_path)
    return storage_filename
