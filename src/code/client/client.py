import requests
import base64
import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem

class ImageSelector(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        # Label et bouton pour l'image
        self.image_label = QLabel('No Image Selected', self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet('color: white; border: 2px solid white; padding: 10px;')
        self.layout.addWidget(self.image_label)

        self.select_image_button = QPushButton('Select Image', self)
        self.select_image_button.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 10px; min-width: 200px;'
        )
        self.layout.addWidget(self.select_image_button)
        self.select_image_button.clicked.connect(self.open_image_dialog)

        # Champ pour saisir le token
        self.token_input = QLineEdit(self)
        self.token_input.setPlaceholderText("Enter your token here")
        self.token_input.setStyleSheet('color: white; background-color: #333; padding: 10px; border: 2px solid white;')
        self.layout.addWidget(self.token_input)

        # Création de la QListWidget
        self.list_widget = QListWidget(self)
        self.list_widget.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 5px;'
        )
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        instructions = ['rotate_left', 'rotate_right', 'inverse', 'b&w', 'grayscale']
        for instruction in instructions:
            item = QListWidgetItem(instruction)
            self.list_widget.addItem(item)
        self.layout.addWidget(self.list_widget)

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
        self.setFixedSize(400, 550)

        # Variable pour stocker le chemin de l'image sélectionnée
        self.image_path = None

    def open_image_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Images (*.png *.xpm *.jpg)', options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
            self.image_path = file_name

    def client(self, image_path, modifications, token):
        mods = ["rotate_left", "rotate_right", "inverse", "b&w", "grayscale"]

        with open(image_path , "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        adresse = "http://10.126.7.74:5000/modification"
        data = {
            'token': token,
            'encoded_image': encoded_image,
            'modifications': modifications
        }
        for modification in modifications:
            if modification not in mods:
                print("Erreur sur une modification.")
                return

        response = requests.post(adresse, json=data)
        decoded_image = base64.b64decode(response.text)
        return decoded_image

    def save_decoded_image(self, decoded_image, image_path, modifications):
        modifications_string = "_".join(modifications)
        output_file = image_path.rsplit('.', 1)[0] + "_" + modifications_string + ".png"
        try:
            with open(output_file, "wb") as decoded_image_file:
                decoded_image_file.write(decoded_image)
            print(f"Image saved as: {output_file}")
            return output_file
        except Exception as e:
            print(f"Error saving image: {str(e)}")
            return None

    def start_processing(self):
        if self.image_path is None:
            QMessageBox.warning(self, 'Warning', 'Please select an image before sending to the server.')
            return

        token = self.token_input.text()
        if not token:
            QMessageBox.warning(self, 'Warning', 'Please enter a valid token.')
            return

        selected_items = self.list_widget.selectedItems()
        modifications = [item.text() for item in selected_items]

        if not modifications:
            QMessageBox.warning(self, 'Warning', 'Please select at least one modification before sending to the server.')
            return

        try:
            decoded_image = self.client(self.image_path, modifications, token)
            if decoded_image:
                pixmap = QPixmap()
                pixmap.loadFromData(decoded_image)
                self.image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
                QMessageBox.information(self, 'Success', 'Image and instruction sent to server!')
            else:
                QMessageBox.information(self, 'failed', 'Failed to process image on the server.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to send data to server: {str(e)}')

app = QApplication(sys.argv)
window = ImageSelector()
window.show()
sys.exit(app.exec_())
