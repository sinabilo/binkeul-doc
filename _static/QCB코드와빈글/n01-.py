from pinkeul.mqb.qcb.qcbplot import QcbPlotter, QBMODE_KEUL
from pinkeul.mqb.qcb.qcbscan import QcbScanner
from pinkeul.mqb.qcb.detechxw import detecHxw
from pinkeul.mqb.vkeul import VKeul 
import pdb
import numpy as np 

from PIL import Image
import matplotlib.pyplot as plt	
from pinkeul.tools.npfunc import pil2np
from pinkeul.tools.cvfunc import showim


HXW = 10

qbp = QcbPlotter(
        HXW,
        step=False,
        ro90=0,
        limit=10,
        qbmode=QBMODE_KEUL,
        k_ex1_pass=True,
        # k_rs_pass=True,k_ex1_pass=True,
        k_rs_pass=True,
        border=True, invert=True)
        
kl = VKeul("yIYuBdUGItwzUjWXSiEAUHDWPUVnYEAVEKPYEwFmtwWVNWZuWVxvtwWVJGEAURLEAVOG")

def n01_():
    data = bytes("그녀는 개와 아이들을 좋아한다./She likes dogs and children.",'utf8')


    ly20,oxm,imc20 = qbp.drawQcb(
        [data],
        # image_slt=bfyim, #mdrim, #manim, #parkim, #
        rsm=30,
        keul=kl,
        realco=True,
        margin=3,
    )
    imc20.show()

    imc20.save('n01-qcb3.png')
    return imc20

# imc20 = n01_()
    



    
def n02_(data,kl,savefile):
    # data = bytes("숲사랑",'utf8')
    # kl = VKeul('WMAWhf')

    # data = bytes("물조심",'utf8')
    # kl = VKeul("UjWwmM")

    # data = bytes("고양이를 찾습니다",'utf8')
    # kl = VKeul("ZuWxtwPwWUWU")

    ly20,oxm,imc20 = qbp.drawQcb(
        [data],
        # image_slt=bfyim, #mdrim, #manim, #parkim, #
        rsm=10,
        keul=kl,
        realco=True,
        margin=3,
    )

    # imc20.show()
    imc20.save(savefile)
    # imc20.save('n11-qcb.png')
    a = QcbScanner.readQcb(imc20,stripmg=True) #,HXW)
    print(a)
    return imc20

    
imc20=n02_(bytes("숲사랑",'utf8'),VKeul('WMAWhf'),savefile='n02-qcb.png')
imc20=n02_(bytes("물조심",'utf8'),VKeul('UjWwmM'),savefile='n03-qcb.png')
imc20=n02_(bytes("고양이를 찾습니다",'utf8'),VKeul('ZuWxtwPwWUWU'),savefile='n010-qcb.png')


# im = Image.open('n11-qcb-ivt.png')
# a = QcbScanner.readQcb(im)#,stripmg=False)
# print( a[-1]['keul'])


    # img = Image 
    # QcvPic()

