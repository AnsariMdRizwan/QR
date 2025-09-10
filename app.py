from flask import Flask, request, jsonify
import qrcode
import io, base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    print("this is data",data)
    upi_id = data.get("upiId")
    name = "Rizwan"
    amount = data.get("amount")

    if not amount:
        return jsonify({"error": "amount naikha bahrle raja"}), 400

    # Create UPI payment link
    payment_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    # Generate QR code
    qr = qrcode.make(payment_link)

    # Save to memory
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    qr_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return jsonify({"qr_code": qr_b64})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
