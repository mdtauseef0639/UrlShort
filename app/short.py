from flask import Blueprint, redirect, jsonify, request, render_template
from app.database import db, ShortenLink as SL

short = Blueprint('short', __name__)


@short.route('/')
def home():
    return render_template('index.html')


@short.route('/short', methods=['POST'])
def short_url():
    original_url = request.form['url']
    link = SL(url=original_url)
    db.session.add(link)
    db.session.commit()

    print(link.code)

    return jsonify(
        code=link.code,
        url=link.url
    )


@short.route('/<code>')
def redirect_to_url(code):
    link = SL.query.filter_by(code=code).first_or_404()
    return redirect(link.url)
