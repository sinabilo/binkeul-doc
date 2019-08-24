from pinkeul.betl.keulplot import hxssPlot
from PIL import Image
from pinkeul.cksetup.btagmap import Btag, BtagMap, BtagmBoxs, drawBtagmBox, hxs_html_img

# drawBtagmBox(20,20).save("brsam01-.png")

img_sam01 = "brsam01-.png"
# img_sam01 = "brsam02-.png"

sam01 = BtagmBoxs(img_sam01)[0,0]

hxss = [ sam01[k].hxs for k in sorted(sam01.keys())]

im = hxssPlot(hxss,unlimit=300,unitsize=4,skewun=3)
im.show()
