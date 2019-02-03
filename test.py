import csv
import cv2
from pytesseract import pytesseract as pt
from pytesseract import Output
import re
import numpy as np

img = cv2.imread('/home/vidit/Desktop/shipmnts/OTH-M/978/3.jpg',0)
h, w= img.shape # assumes color image
boxes = pt.image_to_data(img,output_type=Output.DICT) 
out = pt.image_to_data(img)
txt = pt.image_to_string(img)



def shipper(boxes):
	substr = r"ship"
	substr_1 = r"shpr"
	substrnext = r"to"
	substrname = r"name"
	substrand = r"and"

	substn = r":"
	blank = r""
	data = 0
	for c in range(len(boxes['text'])):
		#print (i)
		i = boxes['text'][c]
		if re.findall(substr,i,re.I) or re.findall(substr_1,i,re.I) :
			
			#print ("Yes",i,c,boxes['left'][c],boxes['top'][c],boxes['width'][c],boxes['height'][c])
			data = c
			#print ("YES",i,type(i),i[-1])

			#cv2.imshow('cut',img[696:730,349:480])
			#cv2.waitKey(0)
			blank_var_1 = re.findall(blank,boxes['text'][c+1],re.I)
			blank_var_2 = re.findall(blank,boxes['text'][c+2],re.I)
			#print (":-",str(boxes['conf'][c+1]))
			#print (":-",str(boxes['conf'][c+2]))


			if  ((int(boxes['conf'][c+1]) != -1  and int(boxes['conf'][c+2]) != -1) or (i[-1] == ':')):
				#print ("************************")
				#print ("->>",boxes['text'][c+1])

				substrnext_var = re.findall(substrnext,boxes['text'][c+1],re.I)
				substn_var = re.findall(substn,boxes['text'][c+1],re.I)
				substrname_var = re.findall(substrname,boxes['text'][c+1],re.I)
				substrand_var = re.findall(substrand,boxes['text'][c+1],re.I)
	 
				#print ("substn_var",len(substn_var))
				#print (len(substrname_var))
				if ( len(substrnext_var) != 0 or len(substn_var)!= 0):
					#print ("YES",boxes['text'][c+1])
					heightofnext = boxes['top'][c+1]
					#print (type(heightofnext),heightofnext)
					consignee_name =[]
					for t in range(5):
						if ( abs(heightofnext- boxes['top'][t+c+1]) < 5):
							#print ("DIfference",boxes['top'][c+1] - int(boxes['top'][i+c+1]))
							consignee_name.append(boxes['text'][t+c+1])
					#cv2.imshow('cut part..',img[boxes['top'][data]:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]+40:boxes['left'][data]+boxes['width'][data]+200])
					#cv2.waitKey(0)		
					#print ("---SHIPPER:---",consignee_name)
					return (consignee_name)
				elif ((i[-1] == ':')):
					#print  ("%##########################$#######")
					heightofnext = boxes['top'][c+1]
					#print (type(heightofnext),heightofnext)
					consignee_name =[]
					for t in range(5):
						if ( abs(heightofnext- boxes['top'][t+c+1]) < 5):
							#print ("DIfference",boxes['top'][c+1] - int(boxes['top'][i+c+1]))
							consignee_name.append(boxes['text'][t+c+1])
					#print ("---Shipper:---",consignee_name)
					return (consignee_name)
				elif ((substrname_var != 0)) :
					#cv2.imshow('cut part',img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
					#cv2.waitKey(0)
					txt = pt.image_to_string(img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
					return  (txt)

					#print ("->>",boxes['text'][c+1])
		
			else :
				#print("BLANK --->>>",boxes['text'][c+1],boxes['text'][c+2])
				#cv2.imshow('cut part',img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+200, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
				#cv2.waitKey(0)
				txt = pt.image_to_string(img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
				return (txt)
def consignee(boxes):
	substr = r"consign"
	substr_1 = r"cons"
	substrnext = r"to"
	substrname = r"name"
	substrand = r"and"

	substn = r":"
	blank = r""
	data = 0
	for c in range(len(boxes['text'])):
		#print (i)
		i = boxes['text'][c]
		if re.findall(substr,i,re.I) or re.findall(substr,i,re.I):
			
			#print ("Yes",i,c,boxes['left'][c],boxes['top'][c],boxes['width'][c],boxes['height'][c])
			data = c
			#print ("YES",i,type(i),i[-1])

			#cv2.imshow('cut',img[696:730,349:480])
			#cv2.waitKey(0)
			blank_var_1 = re.findall(blank,boxes['text'][c+1],re.I)
			blank_var_2 = re.findall(blank,boxes['text'][c+2],re.I)
			#print (":-",str(boxes['conf'][c+1]))
			#print (":-",str(boxes['conf'][c+2]))


			if  ((int(boxes['conf'][c+1]) != -1  and int(boxes['conf'][c+2]) != -1) or (i[-1] == ':')):
				#print ("************************")
				#print ("->>",boxes['text'][c+1])

				substrnext_var = re.findall(substrnext,boxes['text'][c+1],re.I)
				substn_var = re.findall(substn,boxes['text'][c+1],re.I)
				substrname_var = re.findall(substrname,boxes['text'][c+1],re.I)
				substrand_var = re.findall(substrand,boxes['text'][c+1],re.I)
	 
				#print ("substn_var",len(substn_var))
				#print (len(substrname_var))
				if ( len(substrnext_var) != 0 or len(substn_var)!= 0):
					#print ("YES",boxes['text'][c+1])
					heightofnext = boxes['top'][c+1]
					#print (type(heightofnext),heightofnext)
					consignee_name =[]
					for t in range(5):
						if ( abs(heightofnext- boxes['top'][t+c+1]) < 5):
							#print ("DIfference",boxes['top'][c+1] - int(boxes['top'][i+c+1]))
							consignee_name.append(boxes['text'][t+c+1])
					#cv2.imshow('cut part..',img[boxes['top'][data]:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]+40:boxes['left'][data]+boxes['width'][data]+200])
					#cv2.waitKey(0)		
					#print ("---SHIPPER:---",consignee_name)
					return (consignee_name)
				elif ((i[-1] == ':')):
					#print  ("%##########################$#######")
					heightofnext = boxes['top'][c+1]
					#print (type(heightofnext),heightofnext)
					consignee_name =[]
					for t in range(5):
						if ( abs(heightofnext- boxes['top'][t+c+1]) < 5):
							#print ("DIfference",boxes['top'][c+1] - int(boxes['top'][i+c+1]))
							consignee_name.append(boxes['text'][t+c+1])
					#print ("---Shipper:---",consignee_name)
					return (consignee_name)
				elif ((substrname_var != 0)) :
					cv2.imshow('cut part',img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
					cv2.waitKey(0)
					txt = pt.image_to_string(img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
					return  (txt)

					#print ("->>",boxes['text'][c+1])
		
			else :
				#print("BLANK --->>>",boxes['text'][c+1],boxes['text'][c+2])
				cv2.imshow('cut part',img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+200, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
				cv2.waitKey(0)
				txt = pt.image_to_string(img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+200])
				return (txt)
def weight(data):
	w =re.findall(r'\s\d{1,4}[.]\d{1,2}' , data)
	x =re.findall(r'\d{1,5}[,]\d{1,2}',data)
	y =re.findall(r'\d{1,5}[-]\K',data)
	z =re.findall(r'\d{1,5}[.]\d{1,3}[\s]k\w+',data)
	v =re.findall(r'\d{1,5}[\s]\k',data)
	u =re.findall(r'\d{1,5}[;]\d{1,2}',data)
	ws =re.findall(r'\s\d{1,4}[\s][.]\d{1,2}' , data)
	xs =re.findall(r'\s\d{1,4}[,][\s]\d{1,2}' , data)

	#print (xs)

	if (len(z) != 0):
		return z
	elif (len(v) !=0):
		return v
	elif (len(u) != 0):
		return u
	elif (len(x) != 0):
		return x
	elif (len(w) != 0):
		return w
	elif (len(xs) != 0):
		return xs
	elif (len(ws) != 0):
		return ws
	else :
		return ('-')
def dest(data):
	
	substr = r"dst"
	substr_dest = r"dest"
	for c in range(len(boxes['text'])):
		i = boxes['text'][c]
		if re.findall(substr,i,re.I):
			print ("yes",i)
			leftofnext = boxes['left'][c]

			for i in range(30): 
				if ( abs(leftofnext- boxes['left'][i+c+1]) < 20):
					print (boxes['text'][i+c+1])
					return boxes['text'][i+c+1]
		elif re.findall(substr_dest,i,re.I):
			print ("yes",i)
			leftofnext = boxes['left'][c]
			for i in range(30): 
				if ( abs(leftofnext- boxes['left'][i+c+1]) < 20):
					print (boxes['text'][i+c+1])
					return (boxes['text'][i+c+1])
		else :
			return ('-')
def org(data):
	substr = r"org"
	for c in range(len(boxes['text'])):
		i = boxes['text'][c]
		if re.findall(substr,i,re.I):
			print ("yes",i)
			leftofnext = boxes['left'][c]

			for i in range(30): 
				if ( abs(leftofnext- boxes['left'][i+c+1]) < 20):
					print (boxes['text'][i+c+1])
					return boxes['text'][i+c+1]
		else :
			return ('-')
def agent(boxes):
	substr = r"agent"
	substn = r":"
	blank = r""
	data = 0
	for c in range(len(boxes['text'])):
		#print (i)
		i = boxes['text'][c]
		if re.findall(substr,i,re.I):
			
			#print ("Yes",i,c,boxes['left'][c],boxes['top'][c],boxes['width'][c],boxes['height'][c])
			data = c
			#print ("YES",i,type(i),i[-1])

			#cv2.imshow('cut',img[696:730,349:480])
			#cv2.waitKey(0)
			#blank_var_1 = re.findall(blank,boxes['text'][c+1],re.I)
			#blank_var_2 = re.findall(blank,boxes['text'][c+2],re.I)
			#print (":-",str(boxes['conf'][c+1]))
			#print (":-",str(boxes['conf'][c+2]))


			if  ((int(boxes['conf'][c+1]) != -1  and int(boxes['conf'][c+2]) != -1) or (i[-1] == ':')):
				#print ("************************")
				#print ("->>",boxes['text'][c+1])

				substn_var = re.findall(substn,boxes['text'][c+1],re.I)
				#substrname_var = re.findall(substrname,boxes['text'][c+1],re.I)
	 
				#print ("substn_var",len(substn_var))
				#print (len(substrname_var))
				if ( len(substn_var)!= 0):
					#print ("YES",boxes['text'][c+1])
					heightofnext = boxes['top'][c+1]
					#print (type(heightofnext),heightofnext)
					consignee_name =[]
					for t in range(10):
						if ( abs(heightofnext- boxes['top'][t+c+1]) < 5):
							#print ("DIfference",boxes['top'][c+1] - int(boxes['top'][i+c+1]))
							consignee_name.append(boxes['text'][t+c+1])
					#cv2.imshow('cut part..',img[boxes['top'][data]:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]+40:boxes['left'][data]+boxes['width'][data]+200])
					#cv2.waitKey(0)		
					#print ("---SHIPPER:---",consignee_name)
					return (consignee_name)
				elif ((i[-1] == ':')):
					#print  ("%##########################$#######")
					heightofnext = boxes['top'][c+1]
					#print (type(heightofnext),heightofnext)
					consignee_name =[]
					for t in range(10):
						if ( abs(heightofnext- boxes['top'][t+c+1]) < 5):
							#print ("DIfference",boxes['top'][c+1] - int(boxes['top'][i+c+1]))
							consignee_name.append(boxes['text'][t+c+1])
					#print ("---Shipper:---",consignee_name)
					return (consignee_name)
				
					#print ("->>",boxes['text'][c+1])
		
			else :
				print("BLANK --->>>",boxes['text'][c+1],boxes['text'][c+2])
				cv2.imshow('cut part',img[boxes['top'][data]+40:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+250])
				cv2.waitKey(0)
				txt = pt.image_to_string(img[boxes['top'][data]+40:boxes['top'][data]+boxes['height'][data]+80, boxes['left'][data]:boxes['left'][data]+boxes['width'][data]+250])
				return (txt)
def natureofgood(boxes):
	substr = r"nature"
	substn = r":"
	blank = r""
	data = 0
	for c in range(len(boxes['text'])):
		#print (i)
		i = boxes['text'][c]
		if re.findall(substr,i,re.I):
			
			#print ("Yes",i,c,boxes['left'][c],boxes['top'][c],boxes['width'][c],boxes['height'][c])
			data = c
			#cv2.imshow('cut part nature',img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]-30:boxes['left'][data]+boxes['width'][data]+250])
			#cv2.waitKey(0)
			txt = pt.image_to_string(img[boxes['top'][data]+50:boxes['top'][data]+boxes['height'][data]+100, boxes['left'][data]-30:boxes['left'][data]+boxes['width'][data]+250])
			return (txt)
def MAWB(data):
	#txt = pytesseract.image_to_string(img)
	#print (data)
	#print ("****************88")
	x =re.findall(r'\d{3}[-\s]\d{4}[\s]\d{4}[\s]' , data)
	y = re.findall(r'[:]\d{11}', data)
	z = re.findall(r' \d{3}-\d{8}' , data)
	
	print (x,len(x),z)
	exit()
	#if x:
	#	if len(x) < 5:
	#		x = re.findall(r'[:]\d{11}', data)
	#	else:
	#		 pass
	#else:
	#	x = re.findall(r'[:]\d{11}', data)

	print (len(x))
	if (len(x) != 0):
		return x

	elif (len(y) !=0):
		return y
	else :	
		(h, w) = img.shape[:2]
		M = cv2.getRotationMatrix2D((h/2,w/2), 90, 1)
		rotated90 = cv2.warpAffine(img, M, (h, w))
		text90 = pytesseract.image_to_string(img)
		x =re.findall('[0-9][0-9][0-9]-\d{8}',text90)
		boxes = pt.image_to_data(rotated90,output_type=Output.DICT) # also include any config options you use
		out = pt.image_to_data(rotated90)
		if (len(x)!=0):
			return (x,boxes,out,text90)
		else:
			(h, w) = img.shape[:2]
			M = cv2.getRotationMatrix2D((h/2,w/2), 180, 1)
			rotated90 = cv2.warpAffine(img, M, (h, w))
			text90 = pytesseract.image_to_string(rotated90)
			boxes = pt.image_to_data(rotated90,output_type=Output.DICT) # also include any config options you use
			out = pt.image_to_data(rotated90)
			x =re.findall('[0-9][0-9][0-9]-\d{8}',text90)
			if  (len(x) != 0):
				return (x,boxes,out,text90)
			else:
				(h, w) = img.shape[:2]
				M = cv2.getRotationMatrix2D((h/2,w/2), 270, 1)
				rotated90 = cv2.warpAffine(img, M, (h, w))
				boxes = pt.image_to_data(rotated90,output_type=Output.DICT) # also include any config options you use
				out = pt.image_to_data(rotated90)
				text90 = pytesseract.image_to_string(rotated90)
				x =re.findall('[0-9][0-9][0-9]-\d{8}',text90)
				if (len(x) !=0):
					return (x,boxes,out,text90)
				else :
					(h, w) = img.shape[:2]
					M = cv2.getRotationMatrix2D((h/2,w/2), 360, 1)
					rotated90 = cv2.warpAffine(img, M, (h, w))
					boxes = pt.image_to_data(rotated90,output_type=Output.DICT) # also include any config options you use
					out = pt.image_to_data(rotated90)
					text90 = pytesseract.image_to_string(rotated90)
					x =re.findall('[0-9][0-9][0-9]-\d{8}',text90)
					if (len(x) != 0):
						return(x,boxes,out,text90)
					else :
						return (None)






