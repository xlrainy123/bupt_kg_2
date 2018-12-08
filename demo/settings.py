max_nodes_per_level = 10  # 控制每层显示的邻居节点的个数
max_nodes = 20  # 控制路径搜索时，显示每层展示的邻居节点个数
sql_template = 'insert into relationship (source_user,target_user,trust_level) values("{}","{}","{}")'

source_template = '''
    select * from relationship where source_user="{}"
'''
all_template = '''
    select * from relationship where source_user="{}" and target_user="{}"
'''
target_template = '''
    select * from relationship where target_user="{}"
'''
user_profile_template = '''
    insert into weibo_user_profile (usernmame, user_id, weibo_num, following, follower) values("{}","{}","{}","{}","{}") 
'''

user_content_template = '''
    insert into weibo_user_content (usernmame, user_id, weibo_content, weibo_position, publish_time, up_num, repost_num, comment_num, publish_tool) 
    values("{}","{}","{}","{}","{}","{}","{}","{}","{}") 
'''

user_follow_template = '''
    insert into weibo_follow_user (username, user_id, follow_user_name, follow_user_link) values ("{}", "{}","{}","{}")
'''
entity_url = 'https://api.ownthink.com/kg/knowledge?entity={}'
mention_url = 'https://api.ownthink.com/kg/ambiguous?mention={}'
info_url = 'https://api.ownthink.com/bot?token=openbot&info={}'

level_to_int = {
    'Master': 1.0,
    'Journeyer': 0.75,
    'Apprentice': 0.5,
    'Observer': 0.25
}

boson_token = "mp08Nltk.31524.tClWZ2mZX4xF"

topic_to_id = {
    0: '体育',
    1: '教育',
    2: '财经',
    3: '社会',
    4: '娱乐',
    5: '军事',
    6: '国内',
    7: '科技',
    8: '互联网',
    9: '房产',
    10: '国际',
    11: '女性',
    12: '汽车',
    13: '游戏',
}

models = ['general', 'auto', 'kitchen', 'food', 'news', 'weibo']
model_to_name = {
    'general': '通用',
    'auto': '汽车',
    'food': '餐饮',
    'kitchen': '厨具',
    'news': '新闻',
    'weibo': '微博'
}

pos_en_cn = {
    'n':'普通名词',
    'nr':'人名',
    'nz':'其他专名',
    'a':'形容词',
    'm':'数量词',
    'c':'连词',
    'f':'方位名词',
    'ns':'地名',
    'v':'普通动词',
    'ad':'副形词',
    'q':'量词',
    'u':'助词',
    's':'处所名词',
    'nt':'机构团体名',
    'vd':'动副词',
    'an':'名形词',
    'r':'代词',
    'xc':'其他虚词',
    't':'时间名词',
    'nw':'作品名',
    'vn':'名动词',
    'd':'副词',
    'p':'介词',
    'w':'标点符号',
    'PER':'人名',
    'LOC':'地名',
    'ORG':'机构名',
    'TIME':'时间'
}

baidu_access_token = '24.5b454a3cbef9f05ff57c4a98dfc41298.2592000.1545901385.282335-14954286'
baidu_app_id_nlp = '15052604'
baidu_app_key_nlp = '4F1hwLT9H5eHYyL4GWc4BRDK'
baidu_access_token_nlp = 'FCZpazzkIxe1qCm7z3iU2oKbCjcs7XhP'