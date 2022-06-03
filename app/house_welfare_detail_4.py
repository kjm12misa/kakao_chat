from flask import Blueprint
from flask import Flask, request, jsonify
import pandas as pd
import json

# ------------------------------------------------------------------------------------------------------
service_code = {'통합공공임대주택' : 'RH112', '영구임대주택' : 'RH103', '국민임대주택' : 'RH104',
                '장기전세주택' : 'RH105', '공공임대주택' : 'RH106', '전세임대주택' : 'RH107',
                '행복주택' : 'RH108', '공공지원민간임대주택' : 'RH109', '주거복지동주택' : 'RH110',
                '공공기숙사' : 'RH111'}

URL = "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide="
# ------------------------------------------------------------------------------------------------------


blue_house_welfare_detail_4 = Blueprint("house_welfare_detail_4", __name__, url_prefix='/house_welfare_detail_4')

@blue_house_welfare_detail_4.route("/")
def house_welfare__detail_4_home():
    return "house_welfare_detail_4"

@blue_house_welfare_detail_4.route("/show_supply", methods=['POST'])
def show_supply():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    # ----- data url ----------------------------------------------------------------------------
    if welfare_type == '주거복지동주택':
        area_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/dwelling_welfare/supply_area.csv")
        
    else:
        pass
    # -------------------------------------------------------------------------------------------
    
    # ----------------------------------------------
    res = {
    "version": "2.0",
    "template": {
        "outputs": [{
            "carousel" :{
                "type": "itemCard",
                "items": []
            }
        }]
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    # ----------------------------------------------
    if welfare_type == '주거복지동주택':
        for num in range(len(area_data)):
            res['template']['outputs'][0]['carousel']['items'].append({
              "imageTitle": {
                "title": area_data.iloc[num]['business_area'],
                "imageUrl" : ""
              },
              "itemList": [
                {
                  "title": "위치",
                  "description": area_data.iloc[num]['location']
                },
                {
                  "title": "공급호수",
                  "description": area_data.iloc[num]['supply_num']
                },
                {
                  "title" : "착공",
                  "description" : area_data.iloc[num]['construction_start']
                },
                {
                  "title" : "입주자 모집",
                  "description" : area_data.iloc[num]['tenant_recruitment']
                },
                {
                  "title" : "입주 시기",
                  "description" : area_data.iloc[num]['moving_in_time']
                }
              ]
            })
            
        res['template']['outputs'].append({"basicCard": {
                    "title": "주거복지동 사업지구",
                    "thumbnail": {"imageUrl": "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/hwd_map.png",
                                 "link":{"web" : "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/hwd_map.png"}}}})

    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    if welfare_type == '주거복지동주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주 자격·선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)