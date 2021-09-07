from test_task import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_word = db.Column(db.String(50), unique=True, nullable=False)
    match_in_docs = db.Column(db.Integer, nullable=False)

    def __init__(self, name_word, match_in_docs):
        self.name_word = name_word
        self.match_in_docs = match_in_docs

    def __repr__(self):
        return f'<Word: {self.name_word}, matching: {self.match_in_docs}>'