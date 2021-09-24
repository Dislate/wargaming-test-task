from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class UploadFileForm(FlaskForm):
    file_text_doc = FileField()
    submit = SubmitField('Вывести статистику td и idf')
