import psycopg2
from flask import Flask, render_template, request
from psycopg2.errors import UniqueViolation

app = Flask(__name__)
app.debug = True

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="test",
    password="pwd0123456789"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        type_par = request.form['TYPE_PARTICIPANT']
        role = request.form['ROLE_NAME']
        telegram = request.form['telegram']
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO form (email, type_par, role, telegram) VALUES (%s, %s, %s, %s)", (email, type_par, role, telegram))
            conn.commit()
        except (psycopg2.errors.UniqueViolation, psycopg2.errors.NotNullViolation):
            return 'Ошибка! Такой email уже существует'
        return 'Форма отправлена!'
    else:
        return render_template('form.html')



if __name__ == '__main__':
    app.run()