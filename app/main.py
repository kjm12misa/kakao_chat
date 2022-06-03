from flask import Flask, request, Blueprint
import json
import pandas as pd
import csv
import random

from . import region_list
from . import house_welfare
from . import main_menu
from . import house_welfare_detail
from . import house_welfare_detail_1
from . import house_welfare_detail_2
from . import house_welfare_detail_3
from . import house_welfare_detail_4

app = Flask(__name__)

# 지역별 임대주택 목록 출력
app.register_blueprint(region_list.app)
app.register_blueprint(house_welfare.blue_house_welfare)
app.register_blueprint(main_menu.blue_main_menu)
app.register_blueprint(house_welfare_detail.blue_house_welfare_detail)
app.register_blueprint(house_welfare_detail_1.blue_house_welfare_detail_1)
app.register_blueprint(house_welfare_detail_2.blue_house_welfare_detail_2)
app.register_blueprint(house_welfare_detail_3.blue_house_welfare_detail_3)
app.register_blueprint(house_welfare_detail_4.blue_house_welfare_detail_4)




# 헬로우 월드
@app.route('/')
def hello_world():
    return 'Hello, World!'
