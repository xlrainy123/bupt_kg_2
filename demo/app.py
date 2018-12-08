# encoding=utf8
from flask import Flask
from flask import render_template, request
from datetime import timedelta
from util.utils import mention2entity, advogato_data_KG_target, get_paths, \
    advogato_data_KG_source, get_page_rank, KG_View_2
from util.boson import sentiment, tag, classify
import json
from util.semantic import Analysis
import os
from util.baidu import get_baike_url, lexer, emotion
from util.weibo import generate_weibo_user_graph
from settings import model_to_name, models

app = Flask(__name__)
app.config['debug'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route('/about')
def about():
    return render_template('new_year.html')

@app.route('/weibo_search')
def weibo_search():
    return render_template('weibo_search.html')

@app.route('/news')
def news():
    return render_template('attack_earth.html')

@app.route('/')
def hello_world():
    # return render_template('weibo_search.html')
    # return render_template('sentiment.html')
    return render_template('index1.html')
    # return render_template('nlp.html')
    # return render_template('attack_earth.html')

@app.route('/attribute')
def get_attribute():
    pairs = {}
    pairs['1'] = 1
    pairs['2'] = 2
    print(pairs)
    return json.dumps(pairs)

@app.route('/evaluation_2')
def page_rank_2():
    return render_template('page_rank_2.html')

@app.route('/evaluation')
def show_evaluation_results():
    return render_template('page_rank.html')

@app.route('/demo')
def show_demo():
    print("请求方式为:", request.method)
    entity = request.args.to_dict().get('entity', '')
    # mention = request.args.to_dict().get('mention','')
    if entity == '':
        return render_template('demo.html')
    elif "source:" in entity:
        print(entity)
        line = entity.split(':')
        params = line[1].split(",")
        contents = advogato_data_KG_source('source', params[0], int(params[1]))
        print(contents)
        with open("static/data/entity_relationships.json", 'w') as data:
            json.dump(contents, data)
        # name = {"entity":entity, "level":params[1]}
        name = {}
        name['entity'] = str(params[0])
        name['level'] = str(params[1])
        print(name)
        return render_template('entity_relationships.html', contents=name)
    elif "target:" in entity:
        print(entity)
        line = entity.split(':')
        contents = advogato_data_KG_target('target', line[1])
        print(contents)
        return render_template('index.html', contents=contents)
    elif "mention:" in entity:
        print(entity)
        line = entity.strip().split(":")
        mention = line[1]
        contents = mention2entity(mention)
        print(contents)
        with open("static/data/entity_mention.json", 'w') as data:
            json.dump(contents, data)
        urls = {}
        urls['mention'] = mention
        return render_template('entity_mention.html', contents=urls)
    elif "attr:" in entity:
        print(entity)
        line = entity.strip().split(":")
        user = line[1]
        contents = get_page_rank(user)
        print(contents)
        return render_template('index.html', contents=contents)
    elif "path:" in entity:
        print(entity)
        line = entity.strip().split(":")
        entities = line[1].split(",")
        source = entities[0]
        target = entities[1]
        cutoff = entities[2]
        print(source, target, cutoff)
        contents = get_paths(source, target, cutoff)
        with open("static/data/entity_entity_paths.json", 'w') as data:
            json.dump(contents, data)
        paths = {}
        paths['source'] = str(source)
        paths['target'] = str(target)
        paths['cutoff'] = str(cutoff)
        print(paths)
        return render_template('entity_entity_paths.html', contents=paths)
    elif "nlp:" in entity:
        print(entity)
        line = entity.strip().split(":")
        statement = line[1]
        contents = lexer(statement)         # 百度的api
        # slu = Analysis(statement)
        # data = slu.analysis()  # 解析
        # print(data)  # 总的结果
        # print('--------------------------')
        # print("分词：", slu.cws)  # 分词
        # print("词性标注", slu.pos)  # 词性标注
        # print("命名实体识别", slu.ner)  # 命名实体识别
        # print("领域分类", slu.domain)  # 领域分类
        # print("意图识别", slu.intent)  # 意图识别
        # print("槽填充", slu.slot)  # 槽填充
        # contents = {}
        # contents["type"] = "force"
        # categories = []
        # no_repeat_categories = set()
        # for category in slu.pos:
        #     no_repeat_categories.add(category)
        # no_repeat_categories = list(no_repeat_categories)
        # categories_to_int = {}
        # cnt = 0
        # for category in no_repeat_categories:
        #     node = {'name':category, 'keyword':{}, 'base':category}
        #     categories.append(node)
        #     categories_to_int[category] = cnt
        #     cnt += 1
        # node = {'name':'文本语句', 'keyword':{}, 'base':'文本语句'}
        # categories.append(node)
        # categories_to_int['文本语句'] = cnt
        # contents['categories'] = categories
        # nodes = []
        # links = []
        # node = {'name': statement,'value': statement,'category': categories_to_int['文本语句']}
        # nodes.append(node)
        # cnt = 0
        # for word in slu.cws:
        #     node = {'name':word, 'value':str(word), 'category':categories_to_int[slu.pos[cnt]]}
        #     link = {'source':0, 'target':cnt+1, 'value':slu.pos[cnt]}
        #     nodes.append(node)
        #     links.append(link)
        #     cnt += 1
        # contents['nodes'] = nodes
        # contents['links'] = links
        with open("static/data/nlp.json", 'w') as data:
            json.dump(contents, data)
        return render_template('nlp.html')
    elif 'emotion' in entity:
        print(entity)
        line = entity.strip().split(":")
        statement = line[1]
        mydata = emotion(statement)
        # results = sentiment(statement)
        # positive = []
        # negative = []
        # print(results)
        # for model in models:
        #     result = results[model_to_name[model]]
        #     print(result)
        #     positive.append(result[0][0])
        #     negative.append(result[0][1])
        # mydata = {}
        # mydata['positive'] = positive
        # mydata['negative'] = negative
        # mydata['statement'] = statement
        return render_template('sentiment.html', contents=mydata)
    elif 'weibo' in entity:
        print(entity)
        line = entity.strip().split(":")
        user_id = line[1]
        contents, username = generate_weibo_user_graph(user_id=user_id)
        if contents == '':
            return "抱歉，因你过于帅气，我自己都凌乱了。"
        with open("static/data/weibo.json", 'w') as data:
            json.dump(contents, data)
        mydata = {}
        mydata['user_id'] = user_id
        mydata['username'] = username
        return render_template('weibo_graph.html', contents=mydata)
    else:
        file_name = "entity_attribution_{}.json"
        file_path = "static/data/entity_attr/"+file_name.format(entity)
        result = os.path.exists(file_path)
        baidu = {}
        baike_url = get_baike_url(entity)  # 百度百科的url
        baidu['url'] = baike_url
        baidu['entity'] = entity
        if result:
            print("已经有这个文件了")
            return render_template('entity_attribution.html', contents=baidu)
        contents, baike_url = KG_View_2(entity)
        print(contents)
        print(baike_url)
        with open("static/data/entity_attr/"+file_name.format(entity), 'w') as data:
            json.dump(contents, data)
        return render_template('entity_attribution.html', contents=baidu)

@app.route('/search')
def show_search():
    return render_template('search.html')

@app.route('/answer')
def question():
    # print("请求方式为:", request.method)
    # question = request.args.to_dict().get('question', '')
    # if question == '':
    #     return "你可能忘记提问了, 试试/answer?question=刘德华的妻子是谁"
    # print(question)
    # answer = question2info(question)
    # print(answer)
    # return json.dumps(answer, ensure_ascii=False)
    return render_template("robot.html")

@app.route('/mention')
def mention():
    print("请求方式为:", request.method)
    mention = request.args.to_dict().get('mention', '')
    if mention == '':
        return "你可能忘记提问了, 试试/mention?mention=泡泡糖"
    print(mention)
    answers = mention2entity(mention)
    print(answers)
    return json.dumps(answers, ensure_ascii=False)


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
