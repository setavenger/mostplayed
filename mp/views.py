from mp import app
from flask import Flask, render_template, redirect, request, session, make_response
import sys
import config
import base64

reload(sys)
sys.setdefaultencoding('utf-8')

# app = Flask(__name__)
app.config.from_object('config')
client_id = config.client_id


@app.route('/')
@app.route('/index')
def index():
    if request.args.get('ref_code'):
        session.clear()  # to wipe the current sesh
        ref_code = base64.b64decode(request.args.get('ref_code'))
        session['ref_code'] = ref_code
        print(session['ref_code'])
    return render_template('index.html')


@app.route('/go', methods=['GET', 'POST'])
def go():
    session.clear()
    session['num_tracks'] = '50'
    session['time_range'] = request.args.get('time_range')

    print(session['time_range'])

    callback_url = request.url_root + 'callback'
    base_url = 'https://accounts.spotify.com/en/authorize?client_id=' + client_id + '&response_type=code&redirect_uri=' + callback_url + '&scope=user-read-email%20playlist-read-private%20user-follow-read%20user-library-read%20user-top-read%20playlist-modify-private%20playlist-modify-public&state=34fFs29kd09'

    # this is how we set the Cookie when its a Redirect instead of return_response
    # https://stackoverflow.com/questions/12272418/in-flask-set-a-cookie-and-then-re-direct-user
    response = make_response(redirect(base_url, 302))
    response.set_cookie('time_range', request.args.get('time_range'))
    return response
