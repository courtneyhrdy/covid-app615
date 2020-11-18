from flask import Flask, request, render_template
import mysql.connector


app = Flask(__name__)


connection = mysql.connector.connect(host='database-maui.ct7yl5rjhgtx.us-east-1.rds.amazonaws.com',
                                     database='mauidb',
                                     user='admin',
                                     password='Adminpass')


@app.route('/', methods = ['GET','POST'])

def enter_data_values():
    if request.method == 'POST':
        text1 = request.form['scientist']
        text2 = request.form['location']
        text3 = request.form['date']
        text4 = request.form['result']
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO TestTable3 (scientist, location, date, result) VALUES (%s,%s,%s,%s)", (text1, text2, text3, text4))
        connection.commit()
        connection.close


    return render_template('DataEntryUI.html')


if __name__ == '__main__':
    app.run()
    

