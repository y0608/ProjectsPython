from pyzbar import pyzbar
import cv2
import time

cam_port=0

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=3)
    return image

def decode(image):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data[0])
        print()

    return image


if __name__ == "__main__":
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(cam_port)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        
        frame = decode(frame)
        
        
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")
    vc.release()