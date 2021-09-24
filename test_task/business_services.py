from math import log10
from test_task import db, redis_cli
from test_task.models import Word


def handling_words_on_matching_in_doc(list_words_docs, set_words_in_docs):
    """This functions processes all word in uploaded file for getting TF-IDF"""
    result = []
    for word in set_words_in_docs:
        current_word = Word.query.filter_by(name_word=word).first()
        if not current_word:
            new_word = Word(word, 1)
            db.session.add(new_word)
            db.session.commit()
            current_word = new_word
        else:
            current_word.match_in_docs += 1
            db.session.commit()
        count_docs = int(redis_cli.get('count_docs'))
        idf = log10(count_docs / current_word.match_in_docs)
        result.append((word, list_words_docs.count(word), idf))
    return result
