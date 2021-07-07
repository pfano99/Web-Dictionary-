from flask import Flask, render_template, flash
from dict_api import Dictionary
from credentials import language, app_key, app_id
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THEKEY'

class SeachForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    search = SubmitField('Search')

@app.route('/', methods=['POST', 'GET'])
def index():
    form = SeachForm()
    data = None
    if form.validate_on_submit():
        d = Dictionary(app_id=app_id, app_key=app_key, language=language)
        resp = d.search_word(form.word.data)
        if resp:
            data = d.clean_data(resp)
            return render_template('index.html', form=form, data=data)
        else:
            # flash('')
            pass
    return render_template('index.html', form=form, data=data)

if __name__ =='__main__':
    app.run(debug=True)

