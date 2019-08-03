from pinkeul.mqb.qcbv.qcvpic import QcvPic
from PIL import Image
import cv2 

from pinkeul.tools.cvfunc import showim
from pinkeul.tools.cvfunc import rgbread, rgbwrite
from pinkeul.mqb.qcbv.coathsv import coatHsv

# img = Image.open("qv34-org.JPG")

img = rgbread("qv34-org.JPG")

qpc = QcvPic(img)
# qpc = QcvPic("qv34-org.JPG")
    
# r,w,h,e,k = qpc.getQcbData( progress=pgbar )
r,w,h,e,k = qpc.exactQcbData()

