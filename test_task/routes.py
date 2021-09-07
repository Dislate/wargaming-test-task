from flask import request, render_template, url_for
from .forms import UploadFileForm
from test_task import app, db, redis_cli
from test_task.models import Word


@app.route('/', methods=["GET", 'POST'])
def tf_idf():
    form = UploadFileForm()
    total_match = None
    if request.method == "POST":
        # if text document is updated we increment the counter
        redis_cli.incrby('count_docs', 1)
        # get array of all words in document and get array without duplicate
        all_words_in_doc = request.files[form.text_doc.name].read().decode("UTF-8").split()
        set_words = set(all_words_in_doc)
        # init variable idf
        total_match = []
        # processing all words by coincidence
        for word in set_words:
            # checking a word in the database if it exists
            current_word = Word.query.filter_by(name_word=word).first()
            # if it not exists add to db
            if not current_word:
                new_word = Word(word, 1)
                db.session.add(new_word)
                db.session.commit()
                current_word = new_word
            else:
                current_word.match_in_docs += 1
                db.session.commit()
            count_docs = int(redis_cli.get('count_docs'))
            idf = count_docs / current_word.match_in_docs
            total_match.append((word, all_words_in_doc.count(word), idf))
        total_match = sorted(total_match, key=lambda x: x[2])
        print(total_match)
    return render_template('tf-idf.html', form=form, list=total_match)
