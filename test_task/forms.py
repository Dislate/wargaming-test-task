from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

class UploadFileForm(FlaskForm):
    text_doc = FileField()
    submit = SubmitField('Вывести статистикe td и idf')