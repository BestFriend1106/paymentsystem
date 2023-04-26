from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from tronapi import Tron
 app = Flask(__name__)
CORS(app)
 app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///invoices.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 db = SQLAlchemy(app)
 tron = Tron(network="shasta")
 class Invoice(db.Model):
    invoiceId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(10), nullable=False, default="pending")
    txId = db.Column(db.String(50), nullable=True)
     def to_dict(self):
        return {
            "invoiceId": self.invoiceId,
            "name": self.name,
            "email": self.email,
            "amount": self.amount,
            "date": self.date,
            "status": self.status,
        }
 @app.route("/api/invoice", methods=["GET"])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify(invoices=[invoice.to_dict() for invoice in invoices]), 200
 @app.route("/api/invoice", methods=["POST"])
def generate_invoice():
    name = request.json.get("name")
    email = request.json.get("email")
    amount = request.json.get("amount")
     invoice = Invoice(name=name, email=email, amount=amount)
     try:
        db.session.add(invoice)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": "Invoice already exists."}, 409
     return {"invoiceId": invoice.invoiceId}, 201
 @app.route("/api/invoice/<int:invoiceId>", methods=["GET"])
def get_invoice(invoiceId):
    invoice = Invoice.query.get_or_404(invoiceId)
    return jsonify(invoice.to_dict()), 200
 @app.route("/api/invoice/<int:invoiceId>", methods=["PUT"])
def pay_invoice(invoiceId):
    invoice = Invoice.query.get_or_404(invoiceId)
     if invoice.status == "paid":
        return {"error": "Invoice has already been paid."}, 409
     txId = request.json.get("txId")
     try:
        trx = tron.trx.get_transaction(txId)
    except ValueError:
        return {"error": "Invalid transaction ID."}, 400
     if trx["ret"][0]["contractRet"] != "SUCCESS":
        return {"error": "Transaction failed."}, 400
     invoice.status = "paid"
    invoice.txId = txId
     db.session.commit()
     return {"message": "Invoice has been paid."}, 200