from django.core.mail.backends.smtp import EmailBackend
import ssl

class CustomEmailBackend(EmailBackend):
    def open(self):
        # Create a relaxed SSL context
        self.connection = None
        if self.connection:
            return False
        try:
            import smtplib
            context = ssl._create_unverified_context()  # Disable strict TLS check
            self.connection = smtplib.SMTP(self.host, self.port)
            self.connection.ehlo()
            if self.use_tls:
                self.connection.starttls(context=context)
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception as e:
            self.close()
            raise
