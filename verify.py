import requests

class bitpayir:
    api = "*****-*****-*****-********************"
    redirect = "http://yourapiurl.com/callbackurl"


    def request(self, amount, order_id, name, email, description):
        data = {}
        data['api'] = self.api
        data['redirect'] = self.redirect
        data['amount'] = amount

        data['factorId'] = order_id
        data['name'] = name
        data['email'] = email
        data['description'] = description


        response = requests.post('https://bitpay.ir/payment/gateway-send', data)
        return response

    def verify(self, trans_id, id_get):
        data = {}
        data['api'] = self.api
        data['trans_id'] = trans_id
        data['id_get'] = id_get
        data['json'] = 1

        response = requests.post('https://bitpay.ir/payment/gateway-result-second', data)

        return response.json()


gateCall = bitpayir();


result = gateCall.verify('11111', '22222'); #trans_id && id_get
print(result)
##status (all) ,, amount(if successful payment),, cardNum(if successful payment), factorId(if successful payment)
