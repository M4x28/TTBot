from imageai.Detection import ObjectDetection
import os



def getDetection():
  detector = ObjectDetection()

  model_path = "yolo-tiny.h5"
  input_path = "image.jpg"
  output_path = "imagenew.jpg"

  detector.setModelTypeAsTinyYOLOv3()
  detector.setModelPath(model_path)
  detector.loadModel()
  detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
  img = open('imagenew.jpg', 'rb')
  return img