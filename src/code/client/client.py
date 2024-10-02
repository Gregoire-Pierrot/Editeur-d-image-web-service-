import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class ImageSelector(QWidget):

    def __init__(self):
        super().__init__()

        # Connexion au serveur
        client_socket.connect(('localhost', 1234))
        # print(f"Success: connexion with server")

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.image_label = QLabel('No Image Selected', self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet('color: white; border: 2px solid white; padding: 10px;')
        self.layout.addWidget(self.image_label)

        # Bouton pour sélectionner une image
        self.select_image_button = QPushButton('Select Image', self)
        self.select_image_button.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 10px; min-width: 200px;'
        )
        self.layout.addWidget(self.select_image_button)
        self.select_image_button.clicked.connect(self.open_image_dialog)

        # Menu déroulant (combobox) avec des choix d'instructions
        self.combo_box = QComboBox(self)
        self.combo_box.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 5px; min-width: 200px;'
        )
        self.combo_box.addItems(['Instruction 1', 'Instruction 2', 'Instruction 3'])
        self.layout.addWidget(self.combo_box)

        # Bouton pour commencer le traitement
        self.process_button = QPushButton('Send to Server', self)
        self.process_button.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 10px; min-width: 200px;'
        )
        self.layout.addWidget(self.process_button)
        self.process_button.clicked.connect(self.start_processing)

        # Configuration de la fenêtre principale
        self.setLayout(self.layout)
        self.setWindowTitle('Image Selector and Choices')
        self.setStyleSheet('background-color: black;')
        self.setFixedSize(400, 500)

        # Variable pour stocker le chemin de l'image sélectionnée
        self.image_path = None

    def open_image_dialog(self):
        # Ouvre une boîte de dialogue pour sélectionner un fichier image
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Images (*.png *.xpm *.jpg)', options=options)

        # Si un fichier est sélectionné, on l'affiche et on stocke le chemin
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
            self.image_path = file_name

    def start_processing(self):
        # Vérification si une image est sélectionnée
        if self.image_path is None:
            QMessageBox.warning(self, 'Warning', 'Please select an image before sending to the server.')
            return

        # Récupération du choix de l'utilisateur dans la combobox
        selected_instruction = self.combo_box.currentText()

        # Envoi de l'image, instruction et token JWT au serveur
        try:
            self.send_image_and_instruction(self.image_path, selected_instruction)
            QMessageBox.information(self, 'Success', 'Image and instruction sent to server!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to send data to server: {str(e)}')

    def send_image_and_instruction(self, image_path, instruction):
        

        
        jwt_token = 'token'


        #response = client_socket.recv(1024)
        #print(f"Réponse 1 du serveur: {response.decode('ISO-8859-1')}")

        # Attendre que le serveur envoie le token
        #response = client_socket.recv(1024)
        #jwt_token = response.decode('ISO-8859-1').replace("Votre token est ", "")
        #print(f"Token reçu du serveur : {jwt_token}")

        # Lire l'image en binaire
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Encoder l'instruction et le token JWT
        instruction_data = instruction.encode('ISO-8859-1')
        token_data = jwt_token.encode('ISO-8859-1')


        separator = b" "
        requette = token_data + separator + instruction_data + separator + image_data
        print('requette')
        client_socket.sendall(requette)  # Envoyer la requette


        response = client_socket.recv(1024)
        print(f"Réponse du serveur: {response.decode('ISO-8859-1')}")

        client_socket.close()

app = QApplication(sys.argv)
window = ImageSelector()
window.show()
sys.exit(app.exec_())
