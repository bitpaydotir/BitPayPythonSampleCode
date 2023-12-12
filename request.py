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


tempOut = gateCall.request(1000, 1, '09121231231', 'optional', 'optional');
id_get = tempOut.text

###
print(id_get)
### if id_get > 0 then redirect user to  => https://bitpay.ir/payment/gateway-id_get
#############################################
