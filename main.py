from test import *

img = cv2.imread('/home/vidit/Desktop/shipmnts/OTH-M/978/3.jpg',0)
h, w= img.shape # assumes color image
boxes = pt.image_to_data(img,output_type=Output.DICT) 
out = pt.image_to_data(img)
txt = pt.image_to_string(img)

try:
	print ("Shipper ->",shipper(boxes))
	print ("consignee->",consignee(boxes))
	print ("Weight->",weight(txt)) #(txt)
	print ("Dest->",dest(boxes))
	print ("Org->",org(boxes))
	print ("Ageent ->",agent(boxes))
	print ("Nature of Good->",natureofgood(boxes))

except Exception as e :
	print ("Exception Occured",e)