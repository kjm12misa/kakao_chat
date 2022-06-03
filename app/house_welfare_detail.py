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


blue_house_welfare_detail = Blueprint("house_welfare_detail", __name__, url_prefix='/house_welfare_detail')

@blue_house_welfare_detail.route("/")
def house_welfare__detail_home():
    return "house_welfare_detail"

# ----- moving_in_qual_ranking --------------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/moving_in_qual_ranking", methods=['POST'])
def show_moving_in_qual_ranking():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    # ----- data url ---------------------------------------------------------------------------------
    if welfare_type == '영구임대주택':
        moving_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/permanent_lease/Selection_Ranking.csv")
    elif welfare_type == '공공임대주택':
        moving_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_lease/moving_in_selection_rank.csv")
    elif welfare_type == '주거복지동주택':
        moving_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/dwelling_welfare/qualification.csv")
    elif welfare_type == '공공기숙사':
        moving_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_dormitory/selection_criteria.csv")
    else:
        pass
    # ------------------------------------------------------------------------------------------------
    
    if welfare_type == '영구임대주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격 및 선정순위" + "\n\n"
                            + '♤ ' + str(moving_data.iloc[0]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[0]['qualification']) + '\n\n'
                            + str(moving_data.iloc[0]['note'])+ '\n\n\t\t'
                            + '♤ ' + str(moving_data.iloc[1]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[1]['qualification']) + '\n\n'
                            + str(moving_data.iloc[1]['note'])+ '\n\n\t\t'
                            + '♤ ' + str(moving_data.iloc[2]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[2]['qualification']) + '\n\n'}})
    
    elif welfare_type == '공공임대주택': 
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자 선정순위" + "\n\n"
                            + '♤ ' + str(moving_data.iloc[0]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[0]['qualification']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[1]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[1]['qualification'])}})
        
    elif welfare_type == '주거복지동주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격 및 선정순위" + "\n\n"
                            + "- 입주자 모집공고일 현재 해당주택에 임대차 계약을 체결하고 거주중인 기존 임차인으로 아래의 입주자격을 만족하는 자" + '\n\n'
                            + '♤ ' + str(moving_data.iloc[0]['type']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[0]['qualification']) + '\n\n'
                            + str(moving_data.iloc[0]['note'])+ '\n\n\t\t'
                            + '♤ ' + str(moving_data.iloc[1]['type']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[1]['qualification']) + '\n\n'
                            + str(moving_data.iloc[1]['note'])+ '\n\n\t\t'
                            + "- 생계·의료급여수급자 (공공주택특별법 시행규칙의 별표3 제1호 가목, 나목, 다목, 라목의 해당자)" + '\n'
                                                          + "① 국민기초생활보장법상 생계급여수급자 또는 의료급여수급자" + '\n' 
                                                          + "② 국가유공자 등으로서 수급자 선정기준의 소득인정액 이하인 자" + '\n' 
                                                          + "③ 일본군위안부 피해자" + '\n' 
                                                          + "④ 지원대상 한부모가족"                             
                                                         }})
    elif welfare_type == '공공기숙사': 
        res['template']['outputs'].append({"simpleText": {"text": "■ 행복기숙사 신청대상 자격/순위" + "\n\n"
                            + '♤ ' + str(moving_data.iloc[0]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[0]['happy_dormitory']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[1]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[1]['happy_dormitory']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[2]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[2]['happy_dormitory']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[3]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[3]['happy_dormitory']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[4]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[4]['happy_dormitory']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[5]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[5]['happy_dormitory']) + '\n\n'
                            }})
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 희망하우징 신청대상 자격/순위" + "\n\n"
                            + '♤ ' + str(moving_data.iloc[0]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[0]['hope_housing']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[1]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[1]['hope_housing']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[2]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[2]['hope_housing']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[3]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[3]['hope_housing']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[4]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[4]['hope_housing']) + '\n\n'
                            + '♤ ' + str(moving_data.iloc[5]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[5]['hope_housing']) + '\n\n'
                            }})
    
    else:
        pass
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                                                         "thumbnail": {"imageUrl": ""},
                                                         "buttons": [{
                                                                      "label": "링크연결",
                                                                      "action": "webLink",
                                                                      "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    #if welfare_type != '공공임대주택': 
    #    tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
    #                                                "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    if welfare_type == '공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "주택유형", "action": "block", 
                                                     "blockId": "62946260fab76c716dbf5049?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "특별공급", "action": "block", 
                                                     "blockId": "6294626861ca766b95bc3b5c?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "분양전환", "action": "block", 
                                                     "blockId": "6294626efab76c716dbf5061?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    elif welfare_type == '주거복지동주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주 자격·선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    elif welfare_type == '공공기숙사':
        tmp_quickReplies_set['quickReplies'].append({"label": "대상주택", "action": "block", 
                                                     "blockId": "6294627efab76c716dbf5064?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청대상", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    else:
        pass
        
    tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block",
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
        
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)
        
# -------------------------------------------------------------------------------------------------------------------------------------------

# ------ apply_step -------------------------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/apply_step", methods=['POST'])
def show_apply_step():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    # ----- data url -------------------------------------------------------------------------------
    if welfare_type == '통합공공임대주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/total_public/total_public_app_process.csv")
    elif welfare_type == '영구임대주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/permanent_lease/apply_step.csv")
    elif welfare_type == '국민임대주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/kukmin_lease/apply_step.csv")
    elif welfare_type == '공공임대주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_lease/apply_step.csv")
    elif welfare_type == '전세임대주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/deposit_lease/how_apply.csv")
    elif welfare_type == '행복주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/happy_house/apply_step.csv")
    elif welfare_type == '공공지원민간임대주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_support_lease/apply_step.csv")
    elif welfare_type == '주거복지동주택':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/dwelling_welfare/apply_step.csv")
    elif welfare_type == '공공기숙사':
        step_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_dormitory/apply_step.csv")
    else:
        pass
    #-----------------------------------------------------------------------------------------------
    
    if welfare_type == '전세임대주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ " + welfare_type + " 신청절차" + "\n\n"
                            + "1. " + str(step_data.iloc[0]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[0]['how_apply']) + '\n\n'
                            + "2. " + str(step_data.iloc[1]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[1]['how_apply']) + '\n\n'
                            + "3. " + str(step_data.iloc[2]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[2]['how_apply']) + '\n\n'
                            + "4. " + str(step_data.iloc[3]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[3]['how_apply']) + '\n\n'
                            + "5. " + str(step_data.iloc[4]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[4]['how_apply']) + '\n\n'
                            + "6. " + str(step_data.iloc[5]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[5]['how_apply']) + '\n\n'                              
                            + "7. " + str(step_data.iloc[6]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[6]['how_apply']) + '\n\n'                             
                            + "8. " + str(step_data.iloc[7]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[7]['how_apply']) + '\n\n'
                            + "9. " + str(step_data.iloc[8]['subject']) + ' :' + '\n\t\t' + str(step_data.iloc[8]['how_apply']) + '\n\n'                             
                            }})
    
    else:
        res['template']['outputs'].append({"simpleText": {"text": "■ " + welfare_type + " 신청절차" + "\n\n"
                            + "1. " + str(step_data.iloc[0]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[0]['describe']) + '\n\n'
                            + "2. " + str(step_data.iloc[1]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[1]['describe']) + '\n\n'
                            + "3. " + str(step_data.iloc[2]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[2]['describe']) + '\n\n'
                            + "4. " + str(step_data.iloc[3]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[3]['describe']) + '\n\n'
                            + "5. " + str(step_data.iloc[4]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[4]['describe'])}})
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                                                         "thumbnail": {"imageUrl": ""},
                                                         "buttons": [{
                                                                      "label": "링크연결",
                                                                      "action": "webLink",
                                                                      "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    if welfare_type == '통합공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법","action": "block",
                "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '영구임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주·선정순위", "action": "block",
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '국민임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반공급 자격·선정순위", "action": "block", 
                "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정기준", "action": "block", 
                "blockId": "6294624e890e4a16d6ad45f4?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    elif welfare_type == '공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "주택유형", "action": "block", 
                                                     "blockId": "62946260fab76c716dbf5049?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "특별공급", "action": "block", 
                                                     "blockId": "6294626861ca766b95bc3b5c?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "분양전환", "action": "block", 
                                                     "blockId": "6294626efab76c716dbf5061?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '전세임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주대상", "action": "block", 
                                                     "blockId": "62946276603909400c453421?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "대상주택", "action": "block", 
                                                     "blockId": "6294627efab76c716dbf5064?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "전세금지원 한도액", "action": "block", 
                                                     "blockId": "6294628561ca766b95bc3b7f?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "임대조건", "action": "block", 
                                                     "blockId": "6294628efab76c716dbf506b?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "임대기간", "action": "block", 
                                                     "blockId": "62946295fab76c716dbf5090?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '행복주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "최대 거주기간", "action": "block", 
                                                     "blockId": "629462bafab76c716dbf5094?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '공공지원민간임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "상세안내", "action": "block", 
                                                     "blockId": "629462c0fab76c716dbf5096?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '주거복지동주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주 자격·선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '공공기숙사':
        tmp_quickReplies_set['quickReplies'].append({"label": "대상주택", "action": "block", 
                                                     "blockId": "6294627efab76c716dbf5064?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청대상", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청자격·순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    else:
        pass
    
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
        
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)

# -------------------------------------------------------------------------------------------------------------------------------------

# ----- general_supply_selection -------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/general_supply_selection", methods=['POST'])
def show_general_supply_selection():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    # ----- data url ---------------------------------------------------------------------------------------------
    if welfare_type == '통합공공임대주택':
        general_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/total_public/total_public_general_supply_select.csv")
    elif welfare_type == '국민임대주택':
        general_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/kukmin_lease/normal_supply_qual_choose.csv")
    else:
        pass
    #-------------------------------------------------------------------------------------------------------------
    
    if welfare_type == '통합공공임대주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 일반공급 입주자격 및 입주자 선정방법" + "\n\n"
                            + '♤ ' + str(general_data.iloc[0]['class']) + ' : 추첨' + '\n\n\t\t' 
                                                          + str(general_data.iloc[0]['qualification']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[1]['class']) + ' : 추첨' + '\n\n\t\t' 
                                                          + str(general_data.iloc[1]['qualification']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[2]['class']) + ' : 추첨' + '\n\n\t\t' 
                                                          + str(general_data.iloc[2]['qualification']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[3]['class']) + ' : 추첨' + '\n\n\t\t' 
                                                          + str(general_data.iloc[3]['qualification'])}})
    
    elif welfare_type == '국민임대주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 일반공급 입주자격 및 입주자 선정순위" + "\n\n"
                            + '♤ ' + str(general_data.iloc[0]['class']) + ' : ' + '\n\n\t\t' 
                                                          + str(general_data.iloc[0]['qualification']) + '\n\n\t\t'
                                                          + str(general_data.iloc[0]['rank']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[1]['class']) + ' : ' + '\n\n\t\t' 
                                                          + str(general_data.iloc[1]['qualification']) + '\n\n\t\t'
                                                          + str(general_data.iloc[1]['rank'])}})
    else:
        pass
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                                                "thumbnail": {"imageUrl": ""},
                                                "buttons": [{
                                                            "label": "링크연결",
                                                            "action": "webLink",
                                                            "webLinkUrl": URL + service_code[welfare_type]}]}})
        
    tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    if welfare_type == '통합공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '국민임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정기준", "action": "block", 
                "blockId": "6294624e890e4a16d6ad45f4?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    else:
        pass
    
    tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
        
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)
        
# ----------------------------------------------------------------------------------------------------------------------------------

# ----- income_asset_how -----------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/income_asset_how", methods=['POST'])
def show_income_asset_how():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    # ----- data url -------------------------------------------------------------------------------------------
    if welfare_type == '통합공공임대주택':
        income_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/total_public/total_public_members_median_income.csv")
    elif welfare_type == '국민임대주택':
        income_data = pd.read_csv("./app/crawl/service_guide_data/house_welfare/kukmin_lease/income_asset_cal.csv")
    else:
        pass
    # ----------------------------------------------------------------------------------------------------------
    
    if (welfare_type == '통합공공임대주택') or (welfare_type == '국민임대주택'):
        res['template']['outputs'].append({"simpleText": {"text": "■ " + welfare_type + " 소득 · 자산 산정방법" + "\n\n"
                            + '♤ ' + str(income_data.iloc[0]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[0]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[1]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[1]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[2]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[2]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[3]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[3]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[4]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[4]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[5]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[5]['how'])}})
    
    else:
        pass
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                          "thumbnail": {"imageUrl": ""},
                          "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": URL + service_code[welfare_type]}]}})
        
    tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    if welfare_type == '통합공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법", "action": "block",
                "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '국민임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "일반공급 자격·선정순위", "action": "block", 
                "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정기준", "action": "block", 
                "blockId": "6294624e890e4a16d6ad45f4?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    else:
        pass
    
    tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
        
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)
#--------------------------------------------------------------------------------------------------------------------------------------------

# ----- moving_in_qual -----------------------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/moving_in_qual", methods=['POST'])
def show_moving_in_qual():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    # ----- data url ----------------------------------------------------------------------------
    if welfare_type == '통합공공임대주택':
        qual = pd.read_csv("./app/crawl/service_guide_data/house_welfare/total_public/total_public_Tenant_Qual.csv")
    elif welfare_type == '영구임대주택':
        qual = pd.read_csv("./app/crawl/service_guide_data/house_welfare/permanent_lease/homeless_household_note.csv")
    elif welfare_type == '국민임대주택':
        qual = pd.read_csv("./app/crawl/service_guide_data/house_welfare/kukmin_lease/homeless_household_note.csv")
    elif welfare_type == '장기전세주택':
        qual = pd.read_csv("./app/crawl/service_guide_data/house_welfare/long_term_lease/homeless_household_note.csv")
    elif welfare_type == '행복주택':
        qual = pd.read_csv("./app/crawl/service_guide_data/house_welfare/happy_house/moving_in_qual.csv")
    elif welfare_type == '공공기숙사':
        qual = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_dormitory/happy_apply.csv")
        qual_1 = pd.read_csv("./app/crawl/service_guide_data/house_welfare/public_dormitory/hope_apply.csv")
    else:
        pass
    # --------------------------------------------------------------------------------------------
    
    if welfare_type == '통합공공임대주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격" + "\n\n" 
                            + "입주자모집공고일 현재 무주택세대구성원으로서 아래의 소득 및 자산보유 기준에 해당하는 공급신청자격자" + "\n\n"
                            + '- ' + "입주자모집공고일 현재 무주택세대구성원으로서 아래의 소득 및 자산보유기준을 충족하는 자"}})
    
    elif (welfare_type == '영구임대주택') or (welfare_type == '국민임대주택') or (welfare_type == '장기전세주택'):
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격" + "\n\n" 
                            + "입주자모집공고일 현재 무주택세대구성원으로서 아래에 해당하는 공급신청자격자" + "\n\n"
                            + '- ' + "입주자모집공고일 현재 무주택세대구성원으로서 아래의 소득 및 자산보유기준을 충족하는 자"}})
    elif welfare_type == '행복주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격" + "\n\n" 
                            + "입주자 모집공고일 현재 아래의 자격요건에 해당하는 자" + "\n\n"
                            }})
    else:
        pass
    
    if welfare_type == '행복주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 무주택세대구성원" + "\n\n" 
                            + '♤ 계층 :' + str(qual.iloc[0]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[0]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[0]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[1]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[1]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[1]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[2]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[2]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[2]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[3]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[3]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[3]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[4]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[4]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[4]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[5]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[5]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[5]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[6]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[6]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[6]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[7]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[7]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[7]['income_criteria']) + '\n\n'
                            + '♤ 계층 :' + str(qual.iloc[8]['class']) + '\n\n\t\t' 
                                                          + '입주자격 : ' + str(qual.iloc[8]['qualification']) + '\n\n\t\t' 
                                                          +  '소득기준 : ' + str(qual.iloc[8]['income_criteria']) + '\n\n'
                            }})
        
    elif welfare_type == '공공지원민간임대주택':
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격" + "\n\n" 
                            + '♤ ' + '무주택자 우선' + '\n\n'
                            + '♤ ' + '공급물량의 20%이상은 청년·신혼부부 등 주거지원 계층에 특별공급' + '\n\n\t'
                            + '- 주거지원계층 : 도시근로자 평균소득 120% 이하, 19～39세 1인 가구, 혼인 7년 이내 신혼부부, 고령층(65세 이상) 등'}})
        
    elif welfare_type == '공공기숙사':
        res['template']['outputs'].append({"simpleText": {"text": "■ 행복기숙사 신청대상" + "\n\n" 
                            + '♤ ' + str(qual.iloc[0]['room']) + ', ' + str(qual.iloc[2]['room']) + ', ' + str(qual.iloc[4]['room']) + ' :' + '\n\n\t\t' 
                                                          + '* ' + str(qual.iloc[0]['selection']) + '\n\n\t\t'
                                                          + str(qual.iloc[0]['description']) + '\n\n'
                            + '♤ ' + str(qual.iloc[1]['room'])  + ' :' + '\n\n\t\t' 
                                                          + '* ' + str(qual.iloc[1]['selection']) + '\n\n\t\t'
                                                          + str(qual.iloc[1]['description']) + '\n\n'
                            + '♤ ' + str(qual.iloc[3]['room']) + ', ' + str(qual.iloc[5]['room'])  + ' :' + '\n\n\t\t' 
                                                          + '* ' + str(qual.iloc[3]['selection']) + '\n\n\t\t'
                                                          + str(qual.iloc[3]['description'])
                            }})
        res['template']['outputs'].append({"simpleText": {"text": "■ 희망하우징" + "\n\n" 
                            + '♤ ' + str(qual_1.iloc[0]['apply']) + '\n\n\t\t' + str(qual_1.iloc[0]['note'])
                            }})
    
    else:
        res['template']['outputs'].append({"simpleText": {"text": "■ 무주택세대구성원" + "\n\n" 
                            + '♤ ' + str(qual.iloc[1]['member']) + ' :' + '\n\n\t\t' + str(qual.iloc[1]['note']) + '\n\n\n'
                            + '♤ ' + str(qual.iloc[2]['member']) + ' :'  + '\n\n\t\t' + str(qual.iloc[2]['note']) + '\n\n\n'
                            + '♤ ' + str(qual.iloc[3]['member']) + ' :'  + '\n\n\t\t' + str(qual.iloc[3]['note'])}})
    
    res['template']['outputs'].append({"basicCard": {"title": welfare_type + " 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": URL + service_code[welfare_type]}]}})
    
    if welfare_type == '통합공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                                                     "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법", "action": "block",
                                                     "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '영구임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주·선정순위", "action": "block",
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '국민임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                                                     "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반공급 자격·선정순위", "action": "block", 
                                                     "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정기준", "action": "block", 
                                                     "blockId": "6294624e890e4a16d6ad45f4?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '장기전세주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "임대보증금 수준", "action": "block", 
                                                     "blockId": "62946258890e4a16d6ad45f6?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '행복주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "최대 거주기간", "action": "block", 
                                                     "blockId": "629462bafab76c716dbf5094?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '공공지원민간임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "상세안내", "action": "block", 
                                                     "blockId": "629462c0fab76c716dbf5096?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '공공기숙사':
        tmp_quickReplies_set['quickReplies'].append({"label": "대상주택", "action": "block", 
                                                     "blockId": "6294627efab76c716dbf5064?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청자격·순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    else:
        pass
    
    
    if welfare_type != '장기전세주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    else:
        pass
    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block",
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)
    
#----------------------------------------------------------------------------------------------------------------------

# ----- welfare selection ----------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/selection", methods=['POST'])
def blue_house_welfare_detail_selection():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": welfare_type + '\n\n' + "원하시는 상세정보를 선택해주세요."
                }
            }
        ]
    }
}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '통합공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block", 
                                                     "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법", "action": "block", 
                                                     "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '영구임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주·선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '국민임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block", 
                                                     "blockId": "6294622f61ca766b95bc3b48?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반공급 자격·선정순위", "action": "block", 
                                                     "blockId": "62946235603909400c453415?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정기준", "action": "block", 
                                                     "blockId": "6294624e890e4a16d6ad45f4?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '장기전세주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "임대보증금 수준", "action": "block", 
                                                     "blockId": "62946258890e4a16d6ad45f6?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "주택유형", "action": "block", 
                                                     "blockId": "62946260fab76c716dbf5049?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자 선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "특별공급", "action": "block", 
                                                     "blockId": "6294626861ca766b95bc3b5c?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "분양전환", "action": "block", 
                                                     "blockId": "6294626efab76c716dbf5061?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    elif welfare_type == '전세임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주대상", "action": "block", 
                                                     "blockId": "62946276603909400c453421?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "대상주택", "action": "block", 
                                                     "blockId": "6294627efab76c716dbf5064?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "전세금지원 한도액", "action": "block", 
                                                     "blockId": "6294628561ca766b95bc3b7f?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "임대조건", "action": "block", 
                                                     "blockId": "6294628efab76c716dbf506b?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "임대기간", "action": "block", 
                                                     "blockId": "62946295fab76c716dbf5090?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '행복주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "최대 거주기간", "action": "block", 
                                                     "blockId": "629462bafab76c716dbf5094?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    
    elif welfare_type == '공공지원민간임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "상세안내", "action": "block", 
                                                     "blockId": "629462c0fab76c716dbf5096?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        
    elif welfare_type == '주거복지동주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "소개", "action": "block", 
                                                     "blockId": "629462b0890e4a16d6ad45ff?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주 자격·선정순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "공급지역", "action": "block", 
                                                     "blockId": "629462c761ca766b95bc3b82?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    elif welfare_type == '공공기숙사':
        tmp_quickReplies_set['quickReplies'].append({"label": "대상주택", "action": "block", 
                                                     "blockId": "6294627efab76c716dbf5064?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청대상", "action": "block", 
                                                     "blockId": "62946227fab76c716dbf5044?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청자격·순위", "action": "block", 
                                                     "blockId": "6294624661ca766b95bc3b50?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "6294623e890e4a16d6ad45f2?scenarioId=629461f9890e4a16d6ad45e9", "extra": {"welfare_type" : welfare_type}})
    else:
        pass

    tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"})
    tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"})
    
    res['template'].update(tmp_quickReplies_set)
        
    return jsonify(res)
    
    # ---------------------------------------------------------------------------------------------------------------------------------------