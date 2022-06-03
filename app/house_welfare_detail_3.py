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


blue_house_welfare_detail_3 = Blueprint("house_welfare_detail_3", __name__, url_prefix='/house_welfare_detail_3')

@blue_house_welfare_detail_3.route("/")
def house_welfare__detail_3_home():
    return "house_welfare_detail_3"

@blue_house_welfare_detail_3.route("/intro", methods=['POST'])
def show_intro():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    # ----- data url ----------------------------------------------------------------------------
    if welfare_type == '행복주택':
        intro_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/happy_house/feature.csv")
        intro_data_1 = pd.read_csv("./app/crawl/service_guide_data/house_welfare/happy_house/vs_table.csv")
    
    elif welfare_type == '주거복지동주택':
        intro_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/dwelling_welfare/intro.csv")
        
    else:
        pass
    # -------------------------------------------------------------------------------------------
    
    # ----------------------------------------------
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    # ----------------------------------------------
    
    if welfare_type == '행복주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 특장점" + "\n\t" 
                                                      + "젊음에 희망을! 지역에 활기를! 미래를 위해 행복주택이 있습니다." + "\n\n\t"
                                                      + "♤ " + intro_data.iloc[0]['feature'] + '\n\t' 
                                                          + intro_data.iloc[0]['note'] +'\n\n'
                                                      + "♤ " + intro_data.iloc[1]['feature'] + '\n\t' 
                                                          + intro_data.iloc[1]['note'] +'\n\n'
                                                      + "♤ " + intro_data.iloc[2]['feature'] + '\n\t' 
                                                          + intro_data.iloc[2]['note']  + '\n\n\n'
                                                      
                                                      + "♤ " + intro_data_1.iloc[0]['class'] + '\n\t' 
                                                          + intro_data_1.iloc[0]['happy'] +'\n\n'
                                                      + "♤ " + intro_data_1.iloc[1]['class'] + '\n\t' 
                                                          + intro_data_1.iloc[1]['happy'] +'\n\n'
                                                      + "♤ " + intro_data_1.iloc[2]['class'] + '\n\t' 
                                                          + intro_data_1.iloc[2]['happy']
                                                      }})
    elif welfare_type == '공공지원민간임대주택':
        res['template']['outputs'].append({"basicCard": {
                    "title": "공공지원 민간임대주택 인포그래픽",
                    "thumbnail": {"imageUrl": "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/newStay_05.jpg",
                                 "link":{"web" : "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/newStay_05.jpg"}}}})
        res['template']['outputs'].append({"basicCard": {
                    "title": "공급계획",
                    "thumbnail": {"imageUrl": "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/newStay_06.jpg",
                                 "link":{"web" : "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/newStay_06.jpg"}}}})
        
    elif welfare_type == '주거복지동주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 주거복지동 주택사업 소개" + "\n\n\t" 
                                                      + "♤ " + intro_data.iloc[0]['intro'] + '\n\n\t'
                                                      + "♤ " + intro_data.iloc[1]['intro'] + '\n\n\t' 
                                                      + "♤ " + intro_data.iloc[2]['intro']}})
        res['template']['outputs'].append({"basicCard": {
                    "title": "",
                    "thumbnail": {"imageUrl": "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/hwd1_1.jpg",
                                 "link":{"web" : "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/hwd1_1.jpg"}}}})
        
        
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    
    if welfare_type == '행복주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "최대 거주기간", "action": "block", 
                                                     "blockId": "629462bafab76c716dbf5094?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '공공지원민간임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '주거복지동주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주 자격·선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
    
    res['template'].update(tmp_quickReplies_set)
    
    return jsonify(res)

@blue_house_welfare_detail_3.route("/max_term", methods=['POST'])
def show_max_term():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    # ----- data url ----------------------------------------------------------------------------
    if welfare_type == '행복주택':
        term_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/happy_house/max_term.csv")
    # -------------------------------------------------------------------------------------------
    
    # ----------------------------------------------
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    # ----------------------------------------------
    
    res['template']['outputs'].append({"simpleText": {"text": "■ 최대 거주기간" + "\n\n\t" 
                                                      + "♤ " + term_data.iloc[0]['qualification'] + '\n : \n\t' 
                                                          + term_data.iloc[0]['max_term'] + '\n\n' 
                                                      
                                                      + "♤ " + term_data.iloc[1]['qualification'] + '\n : \n\t' 
                                                          + term_data.iloc[1]['max_term'] + '\n\n' 
                                                      
                                                      + "♤ " + term_data.iloc[2]['qualification'] + '\n : \n\t' 
                                                          + term_data.iloc[2]['max_term']
                                                      }})
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    if welfare_type == '행복주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    else:
        pass

    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
    
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)

@blue_house_welfare_detail_3.route("/detail_info", methods=['POST'])
def show_detail_info():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    # ----- data url ----------------------------------------------------------------------------
    if welfare_type == '공공지원민간임대주택':
        info_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_support_lease/detail_info.csv")
    # -------------------------------------------------------------------------------------------
    
    # ----------------------------------------------
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    # ----------------------------------------------
    
    res['template']['outputs'].append({
        "basicCard": {
          "title": "공공지원민간임대주택 상세안내",
          "description": info_data.iloc[4]['site'] + ' : ' +info_data.iloc[4]['address'],
          "thumbnail": {
            "imageUrl": "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/newStay_03.jpg"
          },
          "profile": {
            "imageUrl": "https://www.myhome.go.kr/images/portal/myhomeinfo/guideimg/newStay_03.jpg",
            "nickname": "상세안내"
          },
          "buttons": [
            {
              "action": "webLink",
              "label": info_data.iloc[0]['site'],
              "webLinkUrl": info_data.iloc[0]['address']
            },
            {
              "action": "webLink",
              "label": info_data.iloc[1]['site'],
              "webLinkUrl": info_data.iloc[1]['address']
            },
            {
              "action": "webLink",
              "label": info_data.iloc[2]['site'],
              "webLinkUrl": info_data.iloc[2]['address']
            },
            {
              "action": "webLink",
              "label": info_data.iloc[3]['site'],
              "webLinkUrl": info_data.iloc[3]['address']}]}})
    
    res['template']['outputs'].append({
        "basicCard": {
          "title": "공공지원민간임대주택 상세안내",
          "thumbnail": {
            "imageUrl": ""
          },
          "buttons": [
            {
              "action": "webLink",
              "label": info_data.iloc[3]['site'],
              "webLinkUrl": info_data.iloc[3]['address']}]}})
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    if welfare_type == '공공지원민간임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
    
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)