# Conexion con el servidor de correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv


class EmailSender:
    def __init__(self):
        load_dotenv()
        self.remitente = os.getenv('USER')  
        self.server = smtplib.SMTP('smtp.gmail.com',587)
        self.server.starttls()
        self.server.login(self.remitente,os.getenv('PASS'))
    
    def envio_correo(self, destinatario, asunto, contenido, imagen=None):
        msg = MIMEMultipart()
        msg['Subject'] = asunto
        msg['From'] = self.remitente
        msg['To'] = destinatario
        msg.attach(MIMEText(contenido,'html'))
        if imagen is not None:
            with open(imagen,'rb') as f:
                image = MIMEImage(f.read())
                image.add_header('Content-ID','<image1>')
                msg.attach(image)
        # Enviamos el Correo
        self.server.sendmail(self.remitente,destinatario,msg.as_string())
    
    def cerrar_conexion(self):
        self.server.quit()

# Prueba de funcionalidad
if __name__ == '__main__':
    correo = EmailSender()
    correo.envio_correo('bonattipajuelodiego2406@gmail.com','Test','Contenido')
    correo.cerrar_conexion()