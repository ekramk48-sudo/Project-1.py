
#Answer to the question no-01
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/prime_number/<int:number>")
def check_prime(number):
    return jsonify({"Number": number, "isPrime": is_prime(number)})

if __name__ == "__main__":
    app.run(use_reloader=False)




#Answer to the question no-02

import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/airport/<string:icao>")
def get_airport(icao):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ekramk48@",
        database="flight_game"
    )
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT ident, name, municipality FROM airport WHERE ident = %s", (icao.upper(),))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return jsonify({
        "ICAO": result["ident"],
        "Name": result["name"],
        "Location": result["municipality"]
        })
    return jsonify({"error":"Airport not found"}), 404

if __name__ == "__main__":
    app.run(use_reloader=False)


