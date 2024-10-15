import requests


class PushInPay:

	def __init__(self):
		# self.api_token = "1646|mIBCt9mochpLlV4tyBdePgeoOMGJv4IcHDqGdTVVe1307649"
		self.api_token = "1680|eTSfSd8SmCSXc9Jea6eGFbdvEDqum2l8COcOTIUqdaffc986"
		#self.base_url = "https://api-sandbox.pushinpay.com.br"

		self.base_url = "https://api.pushinpay.com.br"

	def create_qr_code(self, value: int):
		try:
			headers = {
				"Authorization": f"Bearer {self.api_token}",
				"Content-Type": "application/json",
				'Accept': 'application/json'
			}
			data = '{"value": ' + str(value) + '}'
			response = requests.post(self.base_url + '/api/pix/cashIn', headers=headers, data=data)
			if response.status_code != 200:
				raise Exception("Erro ao criar o qr code para pagamento via pix.")

			return response.json()
		except Exception as error:
			print(error)
			raise error

	def check_qrcode_state(self, id: str):
		try:
			headers = {
				"Authorization": f"Bearer {self.api_token}",
				"Content-Type": "application/json",
				'Accept': 'application/json'
			}
			response = requests.get(self.base_url + f"/api/transactions/{id}", headers=headers)
			if response.status_code != 200:
				raise Exception("Erro ao buscar dados do qr code para pagamento via pix.")

			return response.json()
		except Exception as error:
			print(error)
			raise error
