from pinkeul.mqb.qcb.qcbplot import QcbPlotter, QBMODE_KEUL
from pinkeul.mqb.qcb.qcbscan import QcbScanner
from pinkeul.mqb.qcb.detechxw import detecHxw
from pinkeul.mqb.vkeul import VKeul 
import pdb
import numpy as np 

HXW = 10

qbp = QcbPlotter(
        HXW,
        step=False,
        ro90=0,
        limit=26,
        qbmode=QBMODE_KEUL,
        k_ex1_pass=False,
        # k_rs_pass=True,k_ex1_pass=True,
        k_rs_pass=True,
        border=True, invert=False)
        
kl = VKeul("yIYuBdUGItwzUjWXSiEAUHDWPUVnYEAVEKPYEwFmtwWVNWZuWVxvtwWVJGEAURLEAVOG")

def n01_():
    data = bytes("그녀는 개와 아이들을 좋아한다./She likes dogs and children.",'utf8')


    ly20,oxm,imc20 = qbp.drawQcb(
        [data],
        # image_slt=bfyim, #mdrim, #manim, #parkim, #
        rsm=30,
        keul=kl,
        realco=True
    )
    imc20.show()

    imc20.save('n01-qcb3.png')
    return imc20

imc20 = n01_()
    
    
def n02_():
    # data = bytes("숲사랑",'utf8')
    # kl = VKeul('WMAWhf')

    # data = bytes("물조심",'utf8')
    # kl = VKeul("UjWwmM")

    data = bytes("고양이를 찾습니다",'utf8')
    kl = VKeul("ZuWxtwPwWUWU")

    ly20,oxm,imc20 = qbp.drawQcb(
        [data],
        # image_slt=bfyim, #mdrim, #manim, #parkim, #
        rsm=10,
        keul=kl,
        realco=True
    )

    imc20.show()
    # imc20.save('n02-qcb.png')
    # imc20.save('n11-qcb.png')
    a = QcbScanner.readQcb(imc20) #,HXW)

    # img = Image 

    # QcvPic()

