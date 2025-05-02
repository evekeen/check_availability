import argparse
from twilio.rest import Client

def send_sms(message, recipient_number, account_sid, auth_token, twilio_number):
    try:
        client = Client(account_sid, auth_token)
        sms = client.messages.create(
            body=message,
            from_=twilio_number,
            to=recipient_number
        )
        print(f"SMS sent successfully with SID: {sms.sid}")
        return True
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send SMS notifications using Twilio")
    parser.add_argument("message", help="Message to send")
    parser.add_argument("recipient", help="Recipient phone number (with country code, e.g., +1234567890)")
    parser.add_argument("--account_sid", help="Twilio Account SID", required=True)
    parser.add_argument("--auth_token", help="Twilio Auth Token", required=True)
    parser.add_argument("--twilio_number", help="Twilio Phone Number", required=True)
    
    args = parser.parse_args()
    
    send_sms(
        args.message, 
        args.recipient, 
        args.account_sid, 
        args.auth_token, 
        args.twilio_number
    ) 