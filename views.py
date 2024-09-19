from flask import render_template, Blueprint, request, jsonify, url_for

from create_video import make_video

bp = Blueprint('video', __name__, url_prefix='/')


@bp.route('/', methods=['POST', 'GET'])
def get_args():
    title = 'Создать видео'
    return render_template('start_page.html', title=title)


@bp.route('/get_data', methods=['POST', 'GET'])
def get_data():
    path = request.form['inputPath']
    name = request.form['inputName']
    filename = request.form['inputFileName']
    result = make_video(path, name, filename)
    response = jsonify({'file_name': url_for('static', filename=result)})
    return response
