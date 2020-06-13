"""
This bot listens to port 5001 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

ACCESS_TOKEN = "EAAEZBSgfLQ2YBAKBaC5If4I4g5lGq8TinQgirkechfeEcrrkpob76AqlpU6KCJG9CwyTZAevJjBBsZBDzZCJNGtt37d82UsZC7D6xWN7yJ4GX066VZB9qZCCxsCrMBGUOIOhMg3nPROza5xlsppc1TgZB7NxhnC2XjZBL6JnU3kaFLAZDZD"
VERIFY_TOKEN = "fbd9caa0-adb1-11ea-a64d-0242ac130004"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print('OUTPUT:' ,output)
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']                        
                        bot.send_text_message(recipient_id, respuesta(message))
                        #bot.send_message(recipient_id,'mensaje recibido')
                    '''    
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):                                                       
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                    '''
                else:
                    pass
        return "Success"

@app.route("/privacidad/", methods=['GET'])
def privacidad():
    return 'validado'

def respuesta(mensaje):
    if mensaje in ('hola'):
        return 'escriba una palabra (comida, deporte, fruta)'
    elif mensaje in ('comida', 'comidas'):
        return 'lomo saltado, menestron, ceviche'
    elif mensaje in ('deporte', 'deportes'):
        return 'futbol, tenis, natacion'
    elif mensaje in ('fruta', 'frutas'):
        return 'manzana, naranja, platano'
    else:
        return 'escriba otra palabra'

if __name__ == "__main__":
    app.run(port=5001, debug=True)