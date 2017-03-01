from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask_mongoengine import MongoEngine
import datetime
from flask import request
from gevent.wsgi import WSGIServer
from gevent import monkey
from jinja2 import Template
import sys
from settings import SETTINGS as settings1

try:
    from settings_local import SETTINGS as settings2
    settings1.update(settings2)
except ImportError:
    pass

monkey.patch_all()

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': settings1['DB_NAME']}
app.config["SECRET_KEY"] = settings1['DB_KEY']

db = MongoEngine(app)


class Message(db.Document):
    send_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    message = db.StringField(max_length=255, required=True)
    user_id = db.StringField(max_length=255, required=True)


# html for debug
@app.route('/<user_id>')
def form_for_send(user_id):
    html = open('templates/index.html').read()
    template = Template(html)
    return template.render(user_id=user_id)


# send a request to the server
@app.route("/api/<user_id>", methods=['POST'])
def send_request(user_id):
    mes_txt = str(request.form['mes_text'])
    try:
        mes = Message(
        message = mes_txt,
        user_id = user_id)
        mes.save()
    except:
        abort(400)
    return make_response(jsonify({'Message': mes}),200)


# delete old records and return records for user_id
@app.route("/api/<user_id>", methods=['GET'])
def get_messages(user_id):
    try:
        now_date_time = datetime.datetime.now()
        td = now_date_time - settings1['TD_PUBLISHED_MES']
        Message.objects.filter(send_time__lt=td).delete()
        mes = Message.objects.filter(user_id=user_id)
        if len(mes) == 0:
            return make_response(jsonify({'text': 'no requests'}), 200)
    except:
        abort(400)
    return make_response(jsonify({'Message': mes}), 200)



@app.errorhandler(400)
def not_found(error):
    err = str(sys.exc_info()[1]) + str(sys.exc_info()[0]) + str(sys.exc_info()[2])
    return make_response(jsonify({'error': err}), 400)



if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
