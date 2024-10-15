from flask import Blueprint, request, jsonify, session

from app.interfaces.push_in_pay import PushInPay

blueprint = Blueprint("api", __name__, url_prefix="/api")

@blueprint.route('/create_qrcode', methods=["POST"])
def create_qr_code():
	try:
		donate_amount = int(request.get_json()['amount'])
		response = PushInPay().create_qr_code(donate_amount)
		return response
	except ValueError as error:
		return jsonify({"erro": True, "message": "Erro ao criar qr code, valor inserido é inválido."})
	except Exception as error:
		return jsonify({"erro": True, "message": "Erro ao criar qr code, por favor entre em contato conosco."})

@blueprint.route('/qrcode_status/<id>')
def get_qr_code_status(id: str):
	try:
		response = PushInPay().check_qrcode_state(id)
		return response
	except ValueError as error:
		print(f"Erro ao buscar status do qr code: {str(error)}")
		return jsonify({"erro": True, "message": "Erro ao buscar status do qr code, valor inserido é inválido."})
	except Exception as error:
		print(f"Erro ao buscar qr code: {str(error)}")
		return jsonify({"erro": True, "message": "Erro ao buscar status do qr code, por favor entre em contato conosco."})
