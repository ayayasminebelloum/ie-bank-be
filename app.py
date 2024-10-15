from iebank_api import app, db
from flask import request, jsonify
from iebank_api.models import Account  # Import the Account model

@app.route('/accounts', methods=['POST'])
def create_new_account():
    data = request.get_json()
    new_account = Account(name=data['name'], currency=data['currency'], country=data['country'])
    db.session.add(new_account)
    db.session.commit()
    return jsonify({'message': 'Account created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
