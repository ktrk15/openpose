import os
import cv2
import shutil
from tqdm import tqdm

done = set()
allfiles = set()
input_dir = 'input_dir'
output_dir = 'output_dir'

MEMORY_BOUND = 2000000

for name in tqdm(os.listdir(input_dir)):
    in_path = os.path.join(input_dir, name)
    img = cv2.imread(in_path)
    h, w, _ = img.shape
    rw, rh = w//16*16, h//16*16
    while True:
        if MEMORY_BOUND > rw * rh:
            break
        rw = rw - 16
        _h = rw / w * h
        rh = _h//16*16
    key = '{}x{}'.format(int(rw), int(rh))

    key_dir = os.path.join(output_dir, key)
    if not os.path.exists(key_dir):
        os.mkdir(key_dir)
    out_path = os.path.join(key_dir, name)
    shutil.copyfile(in_path, out_path)
