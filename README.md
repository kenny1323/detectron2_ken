
## Detectron2 Demo
DETECTRON2/DEMO

THIS IS ONLY THE CONTENT OF THE DIRECTORY /DETECTRON2/DEMO



##BOX EXTRACTION EXANPLE 
#BASH COMMAND
F="/SUPERDIR1"/allfile/1.png; 
cd /000myfiles/anacondadir1/detectron2/demo
python3 extract_person_box.py --config-file /000myfiles/anacondadir1/detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input $F --opts  MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl &
sleep 3





##MASK EXTRACTION
#BASH COMMAND
F="/SUPERDIR1"/allfile/1000.png; 
cd /000myfiles/anacondadir1/detectron2/demo
python3 extract_mask_cumulative.py --config-file /000myfiles/anacondadir1/detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input $F --opts  MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl &
sleep 3
#The image /detectron2/demo/000028.jpg._out1.png  is an example of mask extraction
#The alpha channel of any pixel of the mask is setted to zero. 


