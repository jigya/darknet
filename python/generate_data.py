# Script to generate all the txt files
# Need to generate all the image files
# Need to generate a txt file for each image file
# https://medium.com/@manivannan_data/how-to-train-yolov2-to-detect-custom-objects-9010df784f36

import glob, os
import cv2
import pickle

training_file_path = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/darknet/data/DolphinData/training_file3.txt"
video_file = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/2Feb13_15to17/[CH01]15_00_00.avi"
boundingBoxesFilePath = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/2Feb13_15to17/SegmentedOutput_Chosen/BoundingBoxes"
outputFilePath = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/darknet/data/DolphinData/2Feb_15to17"


# training_file_path = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/darknet/data/DolphinData/training_file2.txt"
# video_file = "//Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/2Feb13_12to14/[CH01]12_00_00.avi"
# boundingBoxesFilePath = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/2Feb13_12to14/SegmentedOutput_Chosen/BoundingBoxes"
# outputFilePath = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/darknet/data/DolphinData/2Feb_12to14"

# training_file_path = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/darknet/data/DolphinData/training_file.txt"
# video_file = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/2Feb13_8to11/[CH01]08_00_00.avi"
# boundingBoxesFilePath = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/2Feb13_8to11/SegmentedOutput_Chosen/BoundingBoxes"
# outputFilePath = "/Users/jigyayadav/Desktop/UCSDAcads/Quarter4/CSE293.nosync/darknet/data/DolphinData/2Feb_8to11"

testImg = ""

os.chdir(boundingBoxesFilePath)
cap = cv2.VideoCapture(video_file)
total_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
total_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(total_height, total_width)
training_file = open(training_file_path, 'w')
frame_cnt = 1
while True:
	ret, frame = cap.read()
	if frame is None:
		break
	frame_cnt += 1
	png_file = "{0}/Frame_{1}.png".format(boundingBoxesFilePath, frame_cnt)
	try:
		png_fh = open(png_file, "rb")
		png_fh.close()
		frame_copy = frame
		frame_num = frame_cnt
		training_file.write('{0}/img{1}.jpg\n'.format(outputFilePath,frame_num))
		cv2.imwrite('{0}/img{1}.jpg'.format(outputFilePath, frame_num), frame)
		with open("{0}/BoundingBox_Frame_{1}.pkl".format(boundingBoxesFilePath, frame_num), "rb") as fo:
			outfile_txt = open("{0}/img{1}.txt".format(outputFilePath, frame_num), "w")
			boundingRectsList = pickle.load(fo)
			for contour in boundingRectsList:
				x1 = contour[0]
				x2 = contour[0]+contour[2]
				y1 = contour[1]
				y2 = contour[1]+contour[3]
				cv2.rectangle(frame_copy,(x1,y1),(x2,y2),(255,0,0),2)
				x_center = (contour[0]+contour[2]/2)/total_width
				y_center = (contour[1]+contour[3]/2)/total_height
				width = contour[2]/total_width
				height = contour[3]/total_height
				bb = [x_center, y_center, width, height]
				# print(bb)
				outfile_txt.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
			outfile_txt.close()
			cv2.imshow('Original Frame', frame_copy)
			keycode = cv2.waitKey(100)
			quit = ((keycode & 0xFF) == ord('q'))
			if quit:
				break
	except FileNotFoundError:
		# print("Not found")
		pass


# for file in glob.glob("*.png"):
# 	frame_num = int(file.split("_")[1].split(".")[0])
# 	print(file, frame_num)
# 	cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num-1)
# 	ret, frame = cap.read()
# 	cv2.imwrite('{0}/img{1}.jpg'.format(outputFilePath, frame_num), frame)
# 	frame_copy = frame
# 	training_file.write('{0}/img{1}.jpg\n'.format(outputFilePath,frame_num))
# 	with open("{0}/BoundingBox_Frame_{1}.pkl".format(boundingBoxesFilePath, frame_num), "rb") as fo:
# 		outfile_txt = open("{0}/img{1}.txt".format(outputFilePath, frame_num), "w")
# 		boundingRectsList = pickle.load(fo)
# 		for contour in boundingRectsList:
# 			x1 = contour[0]
# 			x2 = contour[0]+contour[2]
# 			y1 = contour[1]
# 			y2 = contour[1]+contour[3]
# 			cv2.rectangle(frame_copy,(x1,y1),(x2,y2),(255,0,0),2)
# 			x_center = contour[0]+contour[2]/2
# 			y_center = contour[1]+contour[3]/2
# 			width = contour[2]/total_width
# 			height = contour[3]/total_height
# 			bb = [x_center, y_center, width, height]
# 			# print(bb)
# 			outfile_txt.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
# 		cv2.imshow('Original Frame', frame_copy)
# 		keycode = cv2.waitKey(10000)
# 		quit = ((keycode & 0xFF) == ord('q'))
# 		if quit:
# 			break

training_file.close()









