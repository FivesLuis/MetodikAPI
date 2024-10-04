from app.messagingServices.whatsappAPI import send_message, message_data


def send_message_service(data):
    return send_message(data)

def get_message_data(data):
    return message_data(data)