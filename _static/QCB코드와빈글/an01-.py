from pinkeul.mqb.qcb.qcbplot import QcbPlotter, QBMODE_KEUL
from pinkeul.mqb.qcb.qcbscan import QcbScanner
from pinkeul.mqb.qcb.detechxw import detecHxw
from pinkeul.mqb.vkeul import VKeul 
import pdb
from PIL import Image

HXW = 10


roN = 1

qbp = QcbPlotter(
        HXW,
        step=False,
        ro90=roN,
        limit=35,
        qbmode=QBMODE_KEUL,
        k_ex1_pass=False,
        # k_rs_pass=True,k_ex1_pass=True,
        k_rs_pass=False,
        border=True,invert=False)
        


kl = VKeul("UJEVGBPvKVeqtwWVJGEAVOQTHIVefEAuaWEAVEKEAVOG")
data = bytes("동물들이 보고 있어요",'utf8')
slim = Image.open('an01-.png')
# slim = Image.open('beetle.jpg')

ly20,oxm,imc20 = qbp.drawQcb(
    [data],
    image_slt=slim,
    rsm=10,
    keul=kl,
    realco=True
    # margin=3
)

imc20.show()

imc20.save('an0{}-qcb.png'.format(roN+1))

# imc20.save('an02-qcb.png')

a = QcbScanner.readQcb(imc20) #,HXW)
print(a)


oxm.getOxImg().show()
# detecHxw(imc20,show=True)