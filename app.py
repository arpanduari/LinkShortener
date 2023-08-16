import pyshorteners
from flask import Flask, render_template, request

app = Flask(__name__)


def create_short_links(url):
    s = pyshorteners.Shortener(timeout=6)
    shorted_links_dict = {
        'tinyurl': s.tinyurl.short(url),
        'clckru': s.clckru.short(url),
        'dagd': s.dagd.short(url),
        'isgd': s.isgd.short(url),
        'osdb': s.osdb.short(url)
    }
    return shorted_links_dict


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['post'])
def shorten_links():
    result_links = create_short_links(request.form['inputURL'])
    return render_template('result.html', shorten_links=result_links)


if __name__ == '__main__':
    app.run()
