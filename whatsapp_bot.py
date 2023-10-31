from twilio.rest import Client


twilio_account_sid = "SK650d6b6c68dc66a357af82bce035c632"
twilio_auth_token = "RandYZLT8gSQLFAdzbZaDu6ZSmaJYoTV"
from_whatsapp_number = "+233547046495"

# Create a Twilio client
client = Client(twilio_account_sid, twilio_auth_token)

# Test authentication by fetching account details
account = client.api.accounts(twilio_account_sid).fetch()
print(f"Account SID: {account.sid}, Friendly Name: {account.friendly_name}")

# Define a list of phone numbers (replace with actual numbers)
recipient_numbers = ["whatsapp:+1234567890", "whatsapp:+9876543210"]

# Craft the message
message_body = "Hello, this is a bulk message from your bot!"

# Send messages to each recipient
for recipient in recipient_numbers:
    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=recipient
    )

    print(f"Message sent to {recipient}: {message.sid}")
