import sys
sys.path.append('/usr/local/python')

import cv2
import json
from openpose import OpenPose

def round16(number):
    '''
    Round number to multiples of 16.
    '''
    return number // 16 * 16

if __name__ == '__main__':
    '''
    Python wrapper can detect only body keypoints.
    '''
    img = cv2.imread("input.png")
    h, w, _ = img.shape

    config = json.load(open('config.json'))
    config['net_resolution'] = '{}x{}'.format(round16(w), round16(h))
    openpose = OpenPose(config)

    arr, out_img = openpose.forward(img, True)
    print(arr)
    cv2.imwrite('output.png', out_img)
