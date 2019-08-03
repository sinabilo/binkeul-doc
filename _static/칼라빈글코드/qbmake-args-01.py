'''
# 나무 
py3 -m pinkeul.utils.qbmake  "나무가겨울을보내는방법더.운여름옷껴입더니겨울엔벗고사는것은...시퍼렇게찬하늘을품에안기위해서였구나"  -r 0 -l40 -g0  -k WMAWhfwJEoBSxpWUFe -s  $namu.png -o  $namu-c.png

# 난초 
py3 -m pinkeul.utils.qbmake  "난초의 꿈과 나비의 꿈이 만나는 곳에 꽃이 피었네"  -r 3 -l55 -k FAxiXQRMECEAtwWqYAuHIvHMWjWqYAuHI -e '난과나비' -s  $nan.png -o  $nan-c.png


# 자전거 
py3 -m pinkeul.utils.qbmake  "두 개의 바퀴로 지구를 굴리니 이르지 못할 곳이 없네"  -r 2 -l40 -k vkGvkCZqWPeu -e '부들과자전거' -s  $byc.png -o  $byc-c.png

# 먼지와 길
py3 -m pinkeul.utils.qbmake  "하늘과강과길이만나는곳,영겁의시공간을우리들의세포가떠돌던그이상도이하도아닌먼지자욱한이곳"  -r 0 -l35 -e 먼지와길 20190303 -k ZqWPeuPZMOAWxpWUFeUjWwmM -s  https://3.bp.blogspot.com/-byHUwOTZJkg/XHy1s8Dj4VI/AAAAAAAAAno/mHw0Zt0IoswrDOaVtI0-NJHDisof3nx5QCLcBGAs/s1600/SAM_3598.JPG -o  $dust-c.png

# 인권선언
py3 -m pinkeul.utils.qbmake  "인권선언" -l 75 -k pPMVKAUjWXSiEAUHDTQQTGSybKVbRyHMVbfEAVEKtxStwzvIQWGltxStwzPCIxFAEAVEKybOUyqtwWVNWWUQVOTEAUsIEAVOGtxStwztxStwzpPMVKAUjWXSiEAUHDZuWVJEEBtXHUaSPLNEAVEKpdSPvJwrWwOGvFUufiEAVOG -o lin 

'''
print( __name__)

ARGS = [
        
    "--ro90", 
        '0',
    
    "--hxw",
        '10',
        
    "--limit",
        '75',
        
    "--slt",
        "https://www.un.org/undss/sites/www.un.org.undss/files/u7/UN_logo.png",
        
    "--out",
        "$human-c.png",
    
    "--keul", "pPMVKAUjWXSiEAUHDTQQTGSybKVbRyHMVbfEAVEKtxStwzvIQWGltxStwzPCIxFAEAVEKybOUyqtwWVNWWUQVOTEAUsIEAVOGtxStwztxStwzpPMVKAUjWXSiEAUHDZuWVJEEBtXHUaSPLNEAVEKpdSPvJwrWwOGvFUufiEAVOG",
    
'''우리는 인류 가족 모두에게, 그들이 원래부터 존엄성과 남들과 똑같은 권리와 남에게 빼앗길 수 없는 권리를 가지고 있다 는 사실을 인정해 주어야만 자유롭고 정의로우며 평화적인 세상의 밑바탕이 마련될 수 있다는 점을 인정한다. 또한 오늘날 국가들 사이에서 친선 관계를 발전시키도록 장려하는 일도 참으로 중요한 과제가 되었다.\n\n유엔 총회는 사회 속에 사는  모든 개인과 모든 조직이 본 선언을 언제나 마음속 깊이 간직하면서, 가르침과 배움을 통해, 이미 독립해 있는 유엔 회원국들의 인민들뿐만 아니라 유엔 회원국들의 법적 관할 아래 있는 '식민지 영토'의 피식민 인민들에게도, 이러한 권리와 자유 를 보편적이고 효과적으로 인정해 주고 지켜 주게 하려고, 모든 인민과 모든 국가가 '다함께 달성해야 할 하나의 공통적인 기준'으로서 이 '세계 인권 선언'을 선포하는'''
    # "data", 가장마지막에 위치해야 함 
    # 'A:=' + bytes(range(100)).hex()  ,
    # 'B:=' + (b'0123456789').hex()    ,

]

# ARGS = []

if __name__ == "__main__" : 
    from pinkeul.utils.qbmake import main
    import sys
    
    main(ARGS)
    
    # a= '''
    # 하늘과 강과 길이 만나는 곳, 
    # 영겁의 시공간을 우리들의 세포가 떠돌던 
    # 그 이상도 이하도 아닌
    # 먼지 자욱한
    # 이 곳
    # '''
    
    
    # a = a.replace(" ",'')
    # a = a.replace("\n",'')
    # print(a)
    
    
    
    