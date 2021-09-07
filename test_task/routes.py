from flask import request, render_template, url_for
from .forms import UploadFileForm
from test_task import app, redis_cli
from test_task.business_services import handling_words_on_matching_in_doc


@app.route('/', methods=["GET", 'POST'])
def tf_idf():
    """This view processes incoming documents
    and returns the first fifty words sorted by IDF"""
    form = UploadFileForm()
    total_match = None
    if request.method == "POST":
        # if text document is updated we increment the counter
        redis_cli.incrby('count_docs', 1)
        # get array of all words in document and get array without duplicate
        all_words_in_doc = request.files[form.text_doc.name].read().decode("UTF-8").split()
        set_words_if_doc = set(all_words_in_doc)
        # processing all words by coincidence
        total_match = sorted(handling_words_on_matching_in_doc(all_words_in_doc, set_words_if_doc),
                             key=lambda x: x[2],
                             reverse=True)
        print(total_match)
    return render_template('tf-idf.html', form=form, list=total_match)
