# from pinkeul.cksetup.btagmap import drawBtagmBox
from pinkeul.cksetup.btagmap import Btag, BtagMap, BtagmBoxs, drawBtagmBox, hxs_html_img
from lxml.html.builder import *
import lxml.etree
import lxml 
from pinkeul.tools.webview import viewhtml
from pathlib import Path
import os 

from br_ipa import BR_IPA


# 발음기호면 [..]
def ipa_um(ipa) : 
    if not ipa :
        return ipa 
    if ord(ipa[0]) >= ord('가') :
        return ipa 
    if ipa[0].isnumeric() :
        return ipa 
    
    return "[ {} ]".format(ipa)
    
    
# html table 생성
class TableMaker : 
    def __init__(self,pic,map,no):
        self.pic = pic
        self.map = map
        self.no = no 
        self.bripa = BR_IPA[self.no] 
        
    def to_ltbl(self):
        map = self.map
        
        tbl = TABLE(cellspacing="10")
    
        for y in range(map.row_len): 
            tr = TR()
            for x in range(map.col_len):
                key = (y,x)
                if key in map : 
                    btag = map[key]
                    hxsimg = hxs_html_img(btag.hxs,scale2x=True)
                    
                    ipa= self.bripa.get(key,'')
                    tr.append( 
                        TD(
                            SUB('{}'.format(key)),
                            BR(),
                            lxml.etree.fromstring(hxsimg),
                            BR(),
                            ipa_um(ipa)
                            
                            # ipa if (not ipa or ord(ipa[0]) >= ord('가')) else "[ {} ]".format(ipa)
                        ) 
                    )
                else : 
                    tr.append( TD() )
                # v = map[y,x]
                # print(v)
            tbl.append(tr)
            
        return tbl 
                
                
        
    def getHtml(self, onlydiv=False): 
        map = self.map
        imgurl = Path(os.path.abspath(self.pic)).as_uri()
        ltbl = self.to_ltbl()
        
        div = DIV(
                CLASS("main"),
                STYLE("td {text-align:center}"),
                H1("빈룬-{}".format(self.no)),
                HR(),
                IMG(src=imgurl,width="600"),
                HR(),
                ltbl, #* html_tables
                HR()
            )
            
            
        if onlydiv : 
            html_bytes = lxml.etree.tostring(div, pretty_print=True)
        else : 
            html = HTML(
                HEAD( 
                    TITLE("빈룬-{}".format(self.no)),
                ),
                BODY( div )
            )
            
            html_bytes = lxml.etree.tostring(html, pretty_print=True)
            
        return html_bytes
            
        # for y in range(map.row_len): 
            # for x in range(map.col_len):
                # if not (y,x) in map : continue
                # v = map[y,x]
                # print(v)
    
        
        
def make_map( pic, img, no ) :
    n = no 
    img_n = img
    map_n = BtagmBoxs(img_n)[0,0]

    pic_n = pic
    tmap = TableMaker(pic_n, map_n,n)

    html = tmap.getHtml(True)
    
    
    
    from os.path import splitext, basename
    html_n = splitext(basename(img_n))[0] + ".html"
    
    p = Path(html_n)
    p.write_bytes(html)
    
    # viewhtml(html,'{}.png'.format(html_n))
    viewhtml(html)
    
    print(sorted(map_n.keys()))

    
# make_map( r"binrune\\20190814_233703.jpg", 
          # r"map_A-.PNG", 
          # "A" )
          
# make_map( r"binrune\\20190814_233710.jpg", 
          # r"map_B-.PNG", 
          # "B" )

# make_map( r"binrune\\20190814_233713.jpg", 
# r"map_C-.PNG", 
# "C" )

make_map( r"binrune\\20190814_233718.jpg", 
r"map_D-.PNG", 
"D" )

'''
img_A = r"map_A-.PNG"
map_A = BtagmBoxs(img_A)[0,0]

pic_A = r"binrune\\20190814_233703.jpg"
tmap = TableMaker(pic_A, map_A,'A')

html = tmap.getHtml()
viewhtml(html)
'''

# drawBtagmBox(10,10).save("map-B.png")
# drawBtagmBox()
