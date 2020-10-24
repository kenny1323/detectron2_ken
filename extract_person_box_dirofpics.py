import sys
from os import listdir
from os.path import isfile, join
import os
import extract_person_box



'''
if len(sys.argv) > 1: 
	dirpath=sys.argv[1]
	print(sys.argv)
else: 
	print('error args')

	
	
onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
print(onlyfiles)
print(onlyfiles[0])
extract_person_box_fullpath='/000myfiles/anacondadir1/detectron2/demo/'+'extract_person_box.py'
'''

'''
for file in onlyfiles:
	input1_jpg=dirpath+file
	print(input1_jpg)
	extract_person_box.main --config-file ../configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input '/000myfiles/photoediting_007/NatlieAustin002/single_004-0796033616740.jpg' --opts MODEL.DEVICE cpu MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
'''

	
	
	
os.system('/000myfiles/anacondadir1/detectron2/demo/extract_person_box.py --config-file /000myfiles/anacondadir1/detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input /000myfiles/photoediting_007/NatlieAustin002/single_004-0796033616740.jpg --opts MODEL.DEVICE cpu MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl')
	
	