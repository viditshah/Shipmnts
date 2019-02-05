from test import *
import cv2
import pandas as pd
import os
filename = '/home/arya/Desktop/shipmnts/OTH-M/2179/6.jpg'
img = cv2.imread(filename,0)
h, w= img.shape
#boxes = pt.image_to_data(img,output_type=Output.DICT) 
#out = pt.image_to_data(img)
txt = pt.image_to_string(img)


#print (out)
#exit()
'''
try:
	mawb,boxes,out,data,img = MAWB(txt,img)

	print ("Shipper ->",shipper(boxes,img))
	print ("consignee->",consignee(boxes,img))
	print ("Weight->",weight(txt))
	print ("Dest ->", dest(boxes))
	print ("Org->",org(boxes))
	print ("Ageent ->",agent(boxes,img))
	print ("Nature of Good->",natureofgood(boxes,img))

except Exception as e :
	print ("Exception Occured",e)


'''

c = 0
for dirpath, dirnames, filenames in (os.walk("/home/arya/Desktop/shipmnts/OTH-M/")):

	for filename in [f for f in filenames if f.endswith(".jpg")]:
		print (os.path.join(dirpath, filename))
		img = cv2.imread(os.path.join(dirpath, filename),0)
		txt = pt.image_to_string(img)
		try:
			#print ("Shipper ->",shipper(boxes))
			mawb,boxes,out,txt,img = MAWB(txt,img)
			#print ("consignee->",consignee(boxes))
			#print ("Weight->",weight(txt)) #(txt)
			#print ("Dest->",dest(boxes))
			#print ("Org->",org(boxes))
			#print ("Ageent ->",agent(boxes))
			#print ("Nature of Good->",natureofgood(boxes))
			final_result_regression = pd.DataFrame({'filename':[str(os.path.join(dirpath, filename))],'mawb':[mawb],'consignee':[str(consignee(boxes,img))],'shipper':[str(shipper(boxes,img))],'wieght':[str(weight(txt))],'dest':[dest(boxes)],'Origin':[org(boxes)],'agent':[agent(boxes,img)],'nature OF good':[natureofgood(boxes,img)]})
			final_result_regression.to_csv('output_Regression.csv',mode='a',header=(c==0),index = True)
			c = c+1
			print (c)

		except Exception as e :
			print ("Exception Occured",e)
	