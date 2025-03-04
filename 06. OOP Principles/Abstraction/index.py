# Abstraction is the method for reduce complexity by hiding unnecessary details from the user.

class EmailService:

    def __connect(self):
        print("Connecting to the email server")

    def _authenticate(self):
        print("Authenticating...")

    def sendEmail(self):
        self.__connect
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from the email server")


email = EmailService()

email.sendEmail()   # Connecting to the email server, Authenticating..., Sending email..., Disconnecting from the email server.
                    # So, the user doesn't need to know about the connection and authentication process.
