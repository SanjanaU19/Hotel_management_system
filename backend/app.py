from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app) # Allow frontend to communicate with backend

def get_db_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="root", 
        database="hotel_mana_system"
    )

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == "kapu" and password == "ashu": # Hardcoded admin from original code
        return jsonify({"success": True, "message": "Welcome Admin!"})

    try:
        conn = get_db_connection()
        my_cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM register WHERE email=%s AND password=%s"
        my_cursor.execute(query, (username, password))
        row = my_cursor.fetchone()
        conn.close()

        if row is None:
            return jsonify({"success": False, "message": "Invalid Username & Password"}), 401
        else:
            return jsonify({"success": True, "message": "Login Successful!", "user": row})

    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "running", "message": "Hotel Backend is Online!"})

@app.route('/api/customers', methods=['GET'])
def get_customers():
    try:
        conn = get_db_connection()
        my_cursor = conn.cursor(dictionary=True)
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": rows})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    try:
        conn = get_db_connection()
        my_cursor = conn.cursor(dictionary=True)
        my_cursor.execute("SELECT * FROM room")
        rows = my_cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": rows})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/details', methods=['GET'])
def get_details():
    try:
        conn = get_db_connection()
        my_cursor = conn.cursor(dictionary=True)
        my_cursor.execute("SELECT * FROM details")
        rows = my_cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": rows})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/customers', methods=['POST'])
def add_customer():
    data = request.json
    try:
        conn = get_db_connection()
        my_cursor = conn.cursor()
        my_cursor.execute(
            "INSERT INTO customer (ref, Name, mother, gender, PostCode, Mobile, Email, Nationality, Idproof, Idnumber, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (data.get('ref'), data.get('Name'), data.get('mother'), data.get('gender'), data.get('PostCode'), data.get('Mobile'), data.get('Email'), data.get('Nationality'), data.get('Idproof'), data.get('Idnumber'), data.get('Address'))
        )
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Customer added successfully!"})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/payment/calculate', methods=['POST'])
def calculate_payment():
    data = request.json
    contact = data.get('contact')
    try:
        conn = get_db_connection()
        my_cursor = conn.cursor(dictionary=True)
        
        my_cursor.execute("SELECT Name FROM customer WHERE Mobile=%s", (contact,))
        cust = my_cursor.fetchone()
        if not cust:
            return jsonify({"success": False, "message": "Contact Not found in Customers!"})
            
        my_cursor.execute("SELECT roomtype, roomavailable, meal, noOfdays FROM room WHERE contact=%s", (contact,))
        room = my_cursor.fetchone()
        if not room:
            return jsonify({"success": False, "message": "No Room Booked for this Contact!"})
            
        meal_prices = {"Breakfast": 300, "Lunch": 500, "Dinner": 700, "All": 1500}
        room_prices = {"Single": 2000, "Double": 3000, "Luxury": 4000}
        
        meal_cost = meal_prices.get(room['meal'], 0) if room['meal'] != "All" else meal_prices["All"]
        room_cost = room_prices.get(room['roomtype'], 0)
        
        total = (meal_cost + room_cost) * float(room['noOfdays'])
        tax = total * 0.09
        final_amt = total + tax
        
        conn.close()
        return jsonify({
            "success": True, 
            "data": {
                "name": cust['Name'],
                "roomno": room['roomavailable'],
                "total": final_amt
            }
        })
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/payment', methods=['POST'])
def save_payment():
    data = request.json
    try:
        from datetime import datetime
        conn = get_db_connection()
        my_cursor = conn.cursor()
        current_date = datetime.now().strftime("%d/%m/%Y")
        
        my_cursor.execute(
            "INSERT INTO payment (contact, name, roomno, total_amount, method, amount_paid, date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (data.get('contact'), data.get('name'), data.get('roomno'), data.get('total_amount'), data.get('method'), data.get('amount_paid'), current_date)
        )
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Payment successful!"})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

@app.route('/api/payments', methods=['GET'])
def get_payments():
    try:
        conn = get_db_connection()
        my_cursor = conn.cursor(dictionary=True)
        my_cursor.execute("SELECT * FROM payment")
        rows = my_cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "data": rows})
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Database Error: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
