import os
import logging
from flask import Flask, render_template, request
import pickle
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_pickle(name):
    path = os.path.join(BASE_DIR, name)
    if not os.path.exists(path):
        logger.error('Missing model/data file: %s', path)
        raise FileNotFoundError(path)
    with open(path, 'rb') as f:
        return pickle.load(f)


popular_dataFrame = load_pickle('popular.pkl')
pt = load_pickle('pt.pkl')
books = load_pickle('books.pkl')
similarity_scores = load_pickle('similarity_scores.pkl')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_dataFrame['Book-Title'].values),
        author=list(popular_dataFrame['Book-Author'].values),
        image=list(popular_dataFrame['Image-URL-M'].values),
        votes=list(popular_dataFrame['num_rating'].values),
        rating=list(popular_dataFrame['avg_rating'].values),
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '').strip()
    if not user_input:
        return render_template('recommend.html', error='Please enter a book title')

    # find index safely
    matches = np.where(pt.index == user_input)[0]
    if len(matches) == 0:
        logger.info('User query not found in index: %s', user_input)
        return render_template('recommend.html', error='No recommendations found for the given title')

    index = matches[0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    logger.info('Recommendations for %s: %s', user_input, data)
    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
