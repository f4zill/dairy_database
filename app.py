from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'cse@123', 
    'database': 'dairy_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html',data='data')

@app.route('/cows')
def cows():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cows")
    cows = cursor.fetchall()
    conn.close()
    return render_template('cows.html',cows=cows)

@app.route('/milk_production')
def milk_production():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM milk_productions")
    records = cursor.fetchall()
    conn.close()
    return render_template('milk_production.html', records=records)


@app.route('/milk_sales')
def milk_sales():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM milk_sales")
    sales = cursor.fetchall()
    conn.close()
    return render_template('milk_sales.html', sales=sales)

@app.route('/staff')
def staff():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Staff")
    staff = cursor.fetchall()
    conn.close()
    return render_template('staff.html', staff=staff)

@app.route('/feed_records')
def feed_records():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM feed_records")
    feeds = cursor.fetchall()
    conn.close()
    return render_template('feed_records.html', feeds=feeds)

@app.route('/medical_records')
def medical_records():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM medical_records")
    records = cursor.fetchall()
    conn.close()
    return render_template('medical_records.html', records=records)

@app.route('/expenses')
def expenses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Expenses")
    expenses = cursor.fetchall()
    conn.close()
    return render_template('expenses.html', expenses=expenses)

@app.route('/add_cow', methods=['GET', 'POST'])
def add_cow():
    if request.method == 'POST':
        tag = request.form['tag']
        breed = request.form['Breed']
        dob = request.form['dob']
        gender = request.form['Gender']
        purchase_date = request.form['purchase_date']
        status = request.form['Status']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cows (tag   , Breed, dob, Gender, purchase_date, Status) VALUES (%s, %s, %s, %s, %s, %s)",
                       (tag, breed, dob, gender, purchase_date, status))
        conn.commit()
        conn.close()
        return redirect(url_for('cows'))
    return render_template('add_cow.html')


@app.route('/add_staff', methods=['GET', 'POST'])
def add_staff():
    if request.method == 'POST':
        name = request.form['Name']
        role = request.form['Role']
        join_date = request.form['JoinDate']
        salary = request.form['Salary']
        contact = request.form['ContactNumber']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO staff (Name, Role, JoinDate, Salary, ContactNumber) VALUES (%s, %s, %s, %s, %s)",
                       (name, role, join_date, salary, contact))
        conn.commit()
        conn.close()
        return redirect(url_for('staff'))
    return render_template('add_staff.html')

@app.route('/add_milk_production', methods=['GET', 'POST'])
def add_milk_production():
    if request.method == 'POST':
        cow_id = request.form['CowID']
        date = request.form['Date']
        morning = request.form['MorningMilkLitres']
        evening = request.form['EveningMilkLitres']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO milk_productions (CowID, Date, MorningMilkLitres, EveningMilkLitres) VALUES (%s, %s, %s, %s)",
                       (cow_id, date, morning, evening))
        conn.commit()
        conn.close()
        return redirect(url_for('milk_production'))
    return render_template('add_milk_production.html')


@app.route('/add_milk_sale', methods=['GET', 'POST'])
def add_milk_sale():
    if request.method == 'POST':
        date = request.form['SaleDate']
        customer = request.form['CustomerName']
        qty = request.form['QuantityLitres']
        rate = request.form['RatePerLitre']
        total = request.form['TotalAmount']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO milk_sales (SaleDate, CustomerName, QuantityLitres, RatePerLitre, TotalAmount) VALUES (%s, %s, %s, %s, %s)",
                       (date, customer, qty, rate, total))
        conn.commit()
        conn.close()
        return redirect(url_for('milk_sales'))
    return render_template('add_milk_sale.html')


@app.route('/add_feed_record', methods=['GET', 'POST'])
def add_feed_record():
    if request.method == 'POST':
        cow_id = request.form['CowID']
        date = request.form['FeedDate']
        feed_type = request.form['FeedType']
        qty = request.form['QuantityKg']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feed_records (CowID, FeedDate, FeedType, QuantityKg) VALUES (%s, %s, %s, %s)",
                       (cow_id, date, feed_type, qty))
        conn.commit()
        conn.close()
        return redirect(url_for('feed_records'))
    return render_template('add_feed_record.html')


@app.route('/add_medical_record', methods=['GET', 'POST'])
def add_medical_record():
    if request.method == 'POST':
        cow_id = request.form['CowID']
        date = request.form['TreatmentDate']
        details = request.form['TreatmentDetails']
        vet = request.form['VetName']
        cost = request.form['Cost']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medical_records (CowID, TreatmentDate, TreatmentDetails, VetName, Cost) VALUES (%s, %s, %s, %s, %s)",
                       (cow_id, date, details, vet, cost))
        conn.commit()
        conn.close()
        return redirect(url_for('medical_records'))
    return render_template('add_medical_record.html')


if __name__ == '__main__':
    app.run(debug=True)