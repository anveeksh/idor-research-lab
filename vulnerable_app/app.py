from flask import Flask, jsonify, request, abort
from models import db, User, Order, Document, Profile
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def get_current_user():
    uid = request.headers.get("X-User-ID")
    if not uid:
        abort(401, description="Missing X-User-ID header")
    return int(uid)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    _ = get_current_user()
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "username": user.username, "email": user.email, "ssn_last4": user.ssn_last4})

@app.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    _ = get_current_user()
    order = Order.query.get_or_404(order_id)
    return jsonify({"id": order.id, "user_id": order.user_id, "item": order.item, "total": order.total})

@app.route("/api/docs/<int:doc_id>", methods=["GET"])
def get_document(doc_id):
    _ = get_current_user()
    doc = Document.query.get_or_404(doc_id)
    return jsonify({"id": doc.id, "title": doc.title, "content": doc.content, "owner_id": doc.owner_id})

@app.route("/api/profiles/<int:profile_id>", methods=["PUT"])
def update_profile(profile_id):
    _ = get_current_user()
    data = request.get_json()
    profile = Profile.query.get_or_404(profile_id)
    for key, val in data.items():
        setattr(profile, key, val)
    db.session.commit()
    return jsonify({"message": "Profile updated", "id": profile.id})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
