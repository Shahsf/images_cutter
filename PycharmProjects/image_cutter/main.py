from PIL import Image
from os import listdir
from os.path import isfile, join
path_to_files = 'C://Example//'
path_to_save_corpimgs = 'D://Example//'
onlyfiles = [f for f in listdir(path_to_files) if isfile(join(path_to_files, f))]
for file in onlyfiles:
    im = Image.open(f'{path_to_files}{file}')
    im_crop = im.crop((0, 0, 180, 180))
    im_crop.save(f'{path_to_save_corpimgs}{file}',quality=95)