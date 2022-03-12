# Vamos a crear una aplicación que nos permita generar códigos QR.
# Para ello, vamos a utilizar la librería qrcode.
# La librería nos permite generar códigos QR.

import sys
import qrcode
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore

# --------------------------------------------------
# Interfaz gráfica
# --------------------------------------------------

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
      uic.loadUi('main.ui', self)
      # On typing in the urltext, change the combotype to http or https
      self.urltext.textChanged.connect(self.change_combotype)
      self.btn.clicked.connect(self.generar_qr)
     
    def change_combotype(self):
      # Obtener el texto desde el qlineEdit
      texto = self.urltext.text()
      # Si el texto empieza con "http://" o "https://"
      if texto.startswith("http://") or texto.startswith("https://"):
        # Cambiar el comboBox a http o https
        if texto.startswith("http://"):
          self.combotype.setCurrentIndex(0)
        else:
          self.combotype.setCurrentIndex(1)
    def generar_qr(self):
      # Borrar el label 
      self.labelimg.clear()

      # Obtener el typo ["http", "https"] desde el comboBox
      tipo = self.combotype.currentText()
      # Obtener el texto desde el qlineEdit
      texto = self.urltext.text()

      # Eliminar "http://" o "https://" del texto
      if tipo == "http":
     
        # Eliminar "http://" del texto
        texto = texto[7:]
      elif tipo == "https":
      
        texto = texto[8:]

      url = tipo + "://" + texto
      # Generar el código QR
      img = self.crear_qr(url)
      qpixmapimage = QPixmap(img)
      self.labelimg.setPixmap(qpixmapimage)

      


    def crear_qr(self, url):
      name = "qr.png"
      
      # Generar el código QR con tamaño 261x181
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=3,
      )
      qr.add_data(url)
      qr.make(fit=True)
      img = qr.make_image()
      img.save(name)
      return name

 


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


# --------------------------------------------------
# Ejecución del programa principal
# --------------------------------------------------

if __name__ == "__main__":
    main()