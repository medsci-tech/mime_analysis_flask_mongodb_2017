from app.models import Doctor
from app.models import CityStatistic
from app.models import SocialCircle
from app.models import OpenClass
from app.models import OpenClassUnit
from app.models import LiveShow
import random
import datetime
from pymongo import MongoClient
from flask import Flask
from app.models import mongodb


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'development_mongodb',
    'host': '127.0.0.1',
    'port': 27017
}
mongodb.init_app(app)


# global variables
disease_list = ['糖尿病', '痛风/高尿酸血症', '甲状腺疾病', '骨代谢性疾病', '其他内分泌疾病']
age_group_list = ['小于18岁', '18-30岁', '31-35岁', '41-45岁', '46-50岁', '51-55岁', '56-60岁', '60岁以上']
doctor_office_list = ['糖尿病科', '内分泌科', '风湿科', '甲乳外科', '甲状腺外科', '综合内科', '全科']
doctor_title_list = ['住院医师', '主治医师', '副主任医师', '主任医师']
show_type_list = ['个人直播', '私教课', '会议直播']
hard_level_list = ['初级','中级','高级']
interest_label_list = ['label1','label2','label3','label4','label5','label6','label7','label8']


def load_doctor():
    docot_list=Doctor.objects().all()
    return docot_list


def getEveryDay(begin_date='2016-01-01', end_date='2017-06-07'):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def loadHospital():
    hospital_list = []
    with open('hospital_all_info_3.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            hospital = line.strip().split(',')
            if len(hospital) > 6:
                hospital = hospital[1:]
            hospital_list.append(hospital)
    return hospital_list


def loadRegion():
    region_list = []
    with open('region_info.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            region = line.strip().split(',')
            region_list.append(region)
    return region_list


def getRandomName():
    a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许']
    a2 = ['理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
          '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
          '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
          '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
          '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
          '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
          '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
          '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
          '病', '始', '达', '深', '完', '今', '提']
    a3 = ['', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
          '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
          '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
          '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
          '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
          '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
          '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
          '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
          '超', '负', '勒', '杂', '醒', '洗', '采', '']
    name = random.choice(a1) + random.choice(a2) + random.choice(a3)
    return name


def init_doctor_data():
    hospital_list = loadHospital()
    date_list = getEveryDay()
    doctor_index = 0
    while (doctor_index < 1000):
        doctor = Doctor()
        doctor.name = getRandomName()
        doctor.age_group = random.choice(age_group_list)
        doctor.disease_list = random.sample(disease_list, random.choice(range(1, len(disease_list), 1)))
        doctor.doctor_office = random.choice(doctor_office_list)
        doctor.doctor_title = random.choice(doctor_title_list)
        doctor.phone = str(random.randrange(18800000001, 18899999999, 1))
        # register_day
        now_date = datetime.datetime.strptime(random.choice(date_list), "%Y-%m-%d")
        doctor.register_year = now_date.year
        doctor.register_month = now_date.month
        doctor.register_day = now_date.day
        # hospital_info
        hospital = random.choice(hospital_list)
        # print(hospital)#test output
        doctor.hospital_name = hospital[0]
        doctor.hospital_level = hospital[1]
        doctor.province = hospital[2]
        doctor.city = hospital[3]
        doctor.longitude = float(hospital[4])
        doctor.latitude = float(hospital[5])
        doctor.save()
        doctor_index += 1


def init_city_statistic_data():
    # generate data
    date_list = getEveryDay()
    region_list = loadRegion()
    for every_date in date_list:
        now_date = datetime.datetime.strptime(every_date, "%Y-%m-%d")
        for every_region in region_list:
            city_statistic = CityStatistic()
            # date
            city_statistic.year = now_date.year
            city_statistic.month = now_date.month
            city_statistic.day = now_date.day
            # region
            city_statistic.province = every_region[0]
            city_statistic.city = every_region[1]
            city_statistic.longitude = float(every_region[2])
            city_statistic.latitude = float(every_region[3])
            # statistic
            city_statistic.register_count = random.randint(0, 200)
            city_statistic.authorize_count = random.randint(0, 80)
            city_statistic.save()


def init_live_show_data():
    doctor_list=load_doctor()
    date_list = getEveryDay()
    for every_date in date_list:
        now_date = datetime.datetime.strptime(every_date, "%Y-%m-%d")
        year = now_date.year
        month = now_date.month
        day = now_date.day
        live_show_cnt = 100
        for i in range(1, live_show_cnt):
            live_show_obj=LiveShow()
            live_show_obj.doctor=random.choice(doctor_list)
            live_show_obj.disease_label = random.choice(disease_list)
            live_show_obj.show_name = '空中直播'+'_'+str(i)
            live_show_obj.show_type = random.choice(show_type_list)
            live_show_obj.disease_label = random.choice(disease_list)
            live_show_obj.show_length = random.randint(1, 100)
            live_show_obj.audience_count = random.randint(1, 100)
            live_show_obj.comment_count = random.randint(1, 100)
            live_show_obj.score_count = random.randint(1, 5)
            live_show_obj.year=year
            live_show_obj.month=month
            live_show_obj.day=day
            live_show_obj.save()


def init_open_class_data():
    doctor_list=load_doctor()
    date_list = getEveryDay()
    for every_date in date_list:
        now_date = datetime.datetime.strptime(every_date, "%Y-%m-%d")
        year = now_date.year
        month = now_date.month
        day = now_date.day
        unit_cnt=20
        class_cnt=30
        for i in range(1, unit_cnt):
            for j in range(1, class_cnt):
                open_class_obj=OpenClass()
                open_class_obj.disease_label = random.choice(disease_list)
                open_class_obj.doctor=random.choice(doctor_list)
                open_class_obj.unit_name = '课程单元'+'_'+str(i)
                open_class_obj.class_name = '课程单元'+'_'+'公开课'+'_'+str(j)
                open_class_obj.interest_label_list=random.sample(interest_label_list, random.choice(range(1, len(interest_label_list), 1)))
                open_class_obj.hard_level = random.choice(hard_level_list)
                open_class_obj.visit_count = random.randint(1, 100)
                open_class_obj.display_count = random.randint(1, 100)
                open_class_obj.comment_count = random.randint(1, 100)
                open_class_obj.ppt_download_count = random.randint(1, 100)
                open_class_obj.year=year
                open_class_obj.month=month
                open_class_obj.day=day
                open_class_obj.save()


def init_open_class_unit_data():
    date_list = getEveryDay()
    for every_date in date_list:
        now_date = datetime.datetime.strptime(every_date, "%Y-%m-%d")
        year = now_date.year
        month = now_date.month
        day = now_date.day
        unit_cnt=20
        class_cnt=30
        for i in range(1, unit_cnt):
            for j in range(1, class_cnt):
                open_class_unit_obj=OpenClassUnit()
                open_class_unit_obj.disease_label = random.choice(disease_list)
                open_class_unit_obj.unit_name = '课程单元'+'_'+str(i)
                open_class_unit_obj.interest_label_list=random.sample(interest_label_list, random.choice(range(1, len(interest_label_list), 1)))
                open_class_unit_obj.hard_level = random.choice(hard_level_list)
                open_class_unit_obj.visit_count = random.randint(1, 100)
                open_class_unit_obj.display_count = random.randint(1, 100)
                open_class_unit_obj.comment_count = random.randint(1, 100)
                open_class_unit_obj.consultation_count = random.randint(1, 100)
                open_class_unit_obj.order_count = random.randint(1, 100)
                open_class_unit_obj.income_amount = random.randint(1, 100)
                open_class_unit_obj.ppt_download_count = random.randint(1, 100)
                open_class_unit_obj.year=year
                open_class_unit_obj.month=month
                open_class_unit_obj.day=day
                open_class_unit_obj.save()



def init_social_circle_data():
    doctor_list=load_doctor()
    date_list = getEveryDay()
    for every_date in date_list:
        now_date = datetime.datetime.strptime(every_date, "%Y-%m-%d")
        year = now_date.year
        month = now_date.month
        day = now_date.day
        social_circle_cnt=200
        for i in range(1, social_circle_cnt):
                circle_name = '群组'+'_'+str(i)
                member_count = random.randint(1, 100)
                topic_count = random.randint(1, 100)
                comment_count = random.randint(1, 100)
                social_circle_obj=SocialCircle()
                social_circle_obj.doctor=random.choice(doctor_list)
                social_circle_obj.year=year
                social_circle_obj.month=month
                social_circle_obj.day=day
                social_circle_obj.circle_name=circle_name
                social_circle_obj.member_count=member_count
                social_circle_obj.topic_count=topic_count
                social_circle_obj.comment_count=comment_count
                social_circle_obj.save()


def test_query_circle():
    docot_obj = Doctor.objects().first()
    print(docot_obj.name)
    circle=SocialCircle.objects(doctor=docot_obj).first()
    print(circle.circle_name)
    print(circle.doctor.name)

# doctor data
init_doctor_data()
# city_statistic_data
init_city_statistic_data()
init_live_show_data()
init_open_class_data()
init_open_class_unit_data()
init_social_circle_data()
#test_query_circle()