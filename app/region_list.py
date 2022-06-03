from flask import Blueprint
from flask import Flask, request, jsonify
import pandas as pd
import csv
import random


app = Blueprint("region_list", __name__)


# 임대주택 목록 출력하는 카드
# 1p 서울, 경기, 인천, 대전, 세종, 부산, 울산, 대구, 광주
# 2p 강원도, 충청남도, 충청북도, 경상남도, 경상북도, 전라남도, 전라북도, 제주특별자치도


###################################################################
# description : 카드에 들어갈 텍스트
# thumbnail(필수) : 카드에 들어갈 이미지
# buttons : 카드 밑에 들어가는 버튼
## action : message 또는 webLink
## label : 버튼에 들어가는 텍스트
## webLinkUrl : 버튼 누르면 연결되는 웹페이지 주소

# quickReplies : 바로 연결 버튼
## action : message 또는 block
## blockId : action이 block일 때 넣는 값

# 블록ID 보는 방법
# 오픈빌더에서 해당 블록에 들어간 후 주소를 보면 중간에 /intent/가 있음
# 그 뒤의 값이 블록ID
###################################################################


###################################################################
# thumbnail 불러오기
thumbnail = pd.read_csv("./app/crawl/region_data/thumbnail/Thumbnail.csv")
thumbnail_arr = []
for i in range(10) :
    thumbnail_arr.append(thumbnail.iloc[i]['thumbnail'])
###################################################################


# 서울시 임대주택 목록
@app.route('/api/seoul', methods=['POST'])
def seoul():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    seoul_notice = pd.read_csv("./app/crawl/region_data/Seoul_notice.csv")
    seoul_url = pd.read_csv("./app/crawl/region_data/Seoul_url.csv")

    # 값을 넣을 배열 선언
    seoul_notice_arr = [] # description에 들어갈 값
    seoul_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        seoul_url_arr.append(seoul_url.iloc[i]['url'])
        seoul_notice_arr.append(seoul_notice.iloc[i]['name'] + "\n공급유형 : " + seoul_notice.iloc[i]['title'] + "\n공고일자 : " + seoul_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    
    for i in range(len(seoul_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": seoul_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[i]
                            }
                        ]
                    })
    
    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
        

    return jsonify(res)


# 경기도 임대주택 목록
@app.route('/api/gyeonggiDo', methods=['POST'])
def gyeonggiDo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    gyeonggi_notice = pd.read_csv("./app/crawl/region_data/Gyeonggi_notice.csv")
    gyeonggi_url = pd.read_csv("./app/crawl/region_data/Gyeonggi_url.csv")

    # 값을 넣을 배열 선언
    gyeonggi_notice_arr = [] # description에 들어갈 값
    gyeonggi_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gyeonggi_url_arr.append(gyeonggi_url.iloc[i]['url'])
        gyeonggi_notice_arr.append(gyeonggi_notice.iloc[i]['name'] + "\n공급유형 : " + gyeonggi_notice.iloc[i]['title'] + "\n공고일자 : " + gyeonggi_notice.iloc[i]['re_date'])
    
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(gyeonggi_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": gyeonggi_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)



# 인천 임대주택 목록
@app.route('/api/incheon', methods=['POST'])
def incheon():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    incheon_notice = pd.read_csv("./app/crawl/region_data/Incheon_notice.csv")
    incheon_url = pd.read_csv("./app/crawl/region_data/Incheon_url.csv")

    # 값을 넣을 배열 선언
    incheon_notice_arr = [] # description에 들어갈 값
    incheon_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        incheon_url_arr.append(incheon_url.iloc[i]['url'])
        incheon_notice_arr.append(incheon_notice.iloc[i]['name'] + "\n공급유형 : " + incheon_notice.iloc[i]['title'] + "\n공고일자 : " + incheon_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(incheon_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": incheon_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)
    
    
# 대전 임대주택 목록
@app.route('/api/daejeon', methods=['POST'])
def daejeon():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    daejeon_notice = pd.read_csv("./app/crawl/region_data/Daejeon_notice.csv")
    daejeon_url = pd.read_csv("./app/crawl/region_data/Daejeon_url.csv")

    # 값을 넣을 배열 선언
    daejeon_notice_arr = [] # description에 들어갈 값
    daejeon_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        daejeon_url_arr.append(daejeon_url.iloc[i]['url'])
        daejeon_notice_arr.append(daejeon_notice.iloc[i]['name'] + "\n공급유형 : " + daejeon_notice.iloc[i]['title'] + "\n공고일자 : " + daejeon_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(daejeon_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": daejeon_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)



# 세종특별자치시 임대주택 목록
@app.route('/api/sejong', methods=['POST'])
def sejong():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    sejong_notice = pd.read_csv("./app/crawl/region_data/Sejong_notice.csv")
    sejong_url = pd.read_csv("./app/crawl/region_data/Sejong_url.csv")

    # 값을 넣을 배열 선언
    sejong_notice_arr = [] # description에 들어갈 값
    sejong_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        sejong_url_arr.append(sejong_url.iloc[i]['url'])
        sejong_notice_arr.append(sejong_notice.iloc[i]['name'] + "\n공급유형 : " + sejong_notice.iloc[i]['title'] + "\n공고일자 : " + sejong_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(sejong_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": sejong_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)
    
    
# 부산 임대주택 목록
@app.route('/api/busan', methods=['POST'])
def busan():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])
    
    ###########################################################
    # csv 파일 불러오기
    busan_notice = pd.read_csv("./app/crawl/region_data/Busan_notice.csv")
    busan_url = pd.read_csv("./app/crawl/region_data/Busan_url.csv")

    # 값을 넣을 배열 선언
    busan_notice_arr = [] # description에 들어갈 값
    busan_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        busan_url_arr.append(busan_url.iloc[i]['url'])
        busan_notice_arr.append(busan_notice.iloc[i]['name'] + "\n공급유형 : " + busan_notice.iloc[i]['title'] + "\n공고일자 : " + busan_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################    

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(busan_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": busan_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)
    
    
# 울산 임대주택 목록
@app.route('/api/ulsan', methods=['POST'])
def ulsan():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    ulsan_notice = pd.read_csv("./app/crawl/region_data/Ulsan_notice.csv")
    ulsan_url = pd.read_csv("./app/crawl/region_data/Ulsan_url.csv")

    # 값을 넣을 배열 선언
    ulsan_notice_arr = [] # description에 들어갈 값
    ulsan_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        ulsan_url_arr.append(ulsan_url.iloc[i]['url'])
        ulsan_notice_arr.append(ulsan_notice.iloc[i]['name'] + "\n공급유형 : " + ulsan_notice.iloc[i]['title'] + "\n공고일자 : " + ulsan_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(ulsan_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": ulsan_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)


# 대구 임대주택 목록
@app.route('/api/daegu', methods=['POST'])
def daegu():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    daegu_notice = pd.read_csv("./app/crawl/region_data/Daegu_notice.csv")
    daegu_url = pd.read_csv("./app/crawl/region_data/Daegu_url.csv")

    # 값을 넣을 배열 선언
    daegu_notice_arr = [] # description에 들어갈 값
    daegu_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        daegu_url_arr.append(daegu_url.iloc[i]['url'])
        daegu_notice_arr.append(daegu_notice.iloc[i]['name'] + "\n공급유형 : " + daegu_notice.iloc[i]['title'] + "\n공고일자 : " + daegu_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(daegu_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": daegu_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    
    res['template'].update(tmp_quickReplies_set)
    
    
    return jsonify(res)
    
    
# 광주 임대주택 목록
@app.route('/api/gwangju', methods=['POST'])
def gwangju():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    gwangju_notice = pd.read_csv("./app/crawl/region_data/Gwangju_notice.csv")
    gwangju_url = pd.read_csv("./app/crawl/region_data/Gwangju_url.csv")

    # 값을 넣을 배열 선언
    gwangju_notice_arr = [] # description에 들어갈 값
    gwangju_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gwangju_url_arr.append(gwangju_url.iloc[i]['url'])
        gwangju_notice_arr.append(gwangju_notice.iloc[i]['name'] + "\n공급유형 : " + gwangju_notice.iloc[i]['title'] + "\n공고일자 : " + gwangju_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(gwangju_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": gwangju_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)



# 강원도 임대주택 목록
@app.route('/api/gangwonDo', methods=['POST'])
def gangwonDo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    gangwon_notice = pd.read_csv("./app/crawl/region_data/Gangwon_notice.csv")
    gangwon_url = pd.read_csv("./app/crawl/region_data/Gangwon_url.csv")

    # 값을 넣을 배열 선언
    gangwon_notice_arr = [] # description에 들어갈 값
    gangwon_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gangwon_url_arr.append(gangwon_url.iloc[i]['url'])
        gangwon_notice_arr.append(gangwon_notice.iloc[i]['name'] + "\n공급유형 : " + gangwon_notice.iloc[i]['title'] + "\n공고일자 : " + gangwon_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(gangwon_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": gangwon_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)
    
    
# 충청남도 임대주택 목록
@app.route('/api/chungcheongNamdo', methods=['POST'])
def chungcheongNamdo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])
    
    ###########################################################
    # csv 파일 불러오기
    chungnam_notice = pd.read_csv("./app/crawl/region_data/Chungnam_notice.csv")
    chungnam_url = pd.read_csv("./app/crawl/region_data/Chungnam_url.csv")

    # 값을 넣을 배열 선언
    chungnam_notice_arr = [] # description에 들어갈 값
    chungnam_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        chungnam_url_arr.append(chungnam_url.iloc[i]['url'])
        chungnam_notice_arr.append(chungnam_notice.iloc[i]['name'] + "\n공급유형 : " + chungnam_notice.iloc[i]['title'] + "\n공고일자 : " + chungnam_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(chungnam_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": chungnam_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)
    

# 충청북도 임대주택 목록
@app.route('/api/chungcheongBukdo', methods=['POST'])
def chungcheongBukdo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    chungbuk_notice = pd.read_csv("./app/crawl/region_data/Chungbuk_notice.csv")
    chungbuk_url = pd.read_csv("./app/crawl/region_data/Chungbuk_url.csv")

    # 값을 넣을 배열 선언
    chungbuk_notice_arr = [] # description에 들어갈 값
    chungbuk_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        chungbuk_url_arr.append(chungbuk_url.iloc[i]['url'])
        chungbuk_notice_arr.append(chungbuk_notice.iloc[i]['name'] + "\n공급유형 : " + chungbuk_notice.iloc[i]['title'] + "\n공고일자 : " + chungbuk_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(chungbuk_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": chungbuk_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)
    
    
# 경상남도 임대주택 목록
@app.route('/api/gyeongsangNamdo', methods=['POST'])
def gyeongsangNamdo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    gyeongnam_notice = pd.read_csv("./app/crawl/region_data/Gyeongnam_notice.csv")
    gyeongnam_url = pd.read_csv("./app/crawl/region_data/Gyeongnam_url.csv")

    # 값을 넣을 배열 선언
    gyeongnam_notice_arr = [] # description에 들어갈 값
    gyeongnam_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gyeongnam_url_arr.append(gyeongnam_url.iloc[i]['url'])
        gyeongnam_notice_arr.append(gyeongnam_notice.iloc[i]['name'] + "\n공급유형 : " + gyeongnam_notice.iloc[i]['title'] + "\n공고일자 : " + gyeongnam_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(gyeongnam_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": gyeongnam_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)


# 경상북도 임대주택 목록
@app.route('/api/gyeongsangBukdo', methods=['POST'])
def gyeongsangBukdo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    gyeongbuk_notice = pd.read_csv("./app/crawl/region_data/Gyeongbuk_notice.csv")
    gyeongbuk_url = pd.read_csv("./app/crawl/region_data/Gyeongbuk_url.csv")

    # 값을 넣을 배열 선언
    gyeongbuk_notice_arr = [] # description에 들어갈 값
    gyeongbuk_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gyeongbuk_url_arr.append(gyeongbuk_url.iloc[i]['url'])
        gyeongbuk_notice_arr.append(gyeongbuk_notice.iloc[i]['name'] + "\n공급유형 : " + gyeongbuk_notice.iloc[i]['title'] + "\n공고일자 : " + gyeongbuk_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(gyeongbuk_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": gyeongbuk_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)

    
# 전라남도 임대주택 목록
@app.route('/api/jeollaNamdo', methods=['POST'])
def jeollaNamdo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    jeonnam_notice = pd.read_csv("./app/crawl/region_data/Jeonnam_notice.csv")
    jeonnam_url = pd.read_csv("./app/crawl/region_data/Jeonnam_url.csv")

    # 값을 넣을 배열 선언
    jeonnam_notice_arr = [] # description에 들어갈 값
    jeonnam_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        jeonnam_url_arr.append(jeonnam_url.iloc[i]['url'])
        jeonnam_notice_arr.append(jeonnam_notice.iloc[i]['name'] + "\n공급유형 : " + jeonnam_notice.iloc[i]['title'] + "\n공고일자 : " + jeonnam_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(jeonnam_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": jeonnam_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)

    

# 전라북도 임대주택 목록
@app.route('/api/jeollaBukdo', methods=['POST'])
def jeollaBukdo():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    jeonbuk_notice = pd.read_csv("./app/crawl/region_data/Jeonbuk_notice.csv")
    jeonbuk_url = pd.read_csv("./app/crawl/region_data/Jeonbuk_url.csv")

    # 값을 넣을 배열 선언
    jeonbuk_notice_arr = [] # description에 들어갈 값
    jeonbuk_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        jeonbuk_url_arr.append(jeonbuk_url.iloc[i]['url'])
        jeonbuk_notice_arr.append(jeonbuk_notice.iloc[i]['name'] + "\n공급유형 : " + jeonbuk_notice.iloc[i]['title'] + "\n공고일자 : " + jeonbuk_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(jeonbuk_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": jeonbuk_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)
    
    
# 제주특별자치도 임대주택 목록
@app.route('/api/jeju', methods=['POST'])
def jeju():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    jeju_notice = pd.read_csv("./app/crawl/region_data/Jeju_notice.csv")
    jeju_url = pd.read_csv("./app/crawl/region_data/Jeju_url.csv")

    # 값을 넣을 배열 선언
    jeju_notice_arr = [] # description에 들어갈 값
    jeju_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        jeju_url_arr.append(jeju_url.iloc[i]['url'])
        jeju_notice_arr.append(jeju_notice.iloc[i]['name'] + "\n공급유형 : " + jeju_notice.iloc[i]['title'] + "\n공고일자 : " + jeju_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    res= {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "basicCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    for i in range(len(jeju_notice_arr)):
        res['template']['outputs'][0]['carousel']['items'].append({
                        "description": jeju_notice_arr[i],
                        "thumbnail": {
                            "imageUrl": rand_thumb[i]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[i]
                            }
                        ]
                    })

    tmp_quickReplies_set['quickReplies'].append({
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        })
    tmp_quickReplies_set['quickReplies'].append({
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        })
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)
    