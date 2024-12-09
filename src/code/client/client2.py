import requests
import base64
import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, \
    QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem


class ImageSelector(QWidget):

    def __init__(self):
        super().__init__()

        self.modified_image = None

        # Créer un layout principal
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        # Créer un layout horizontal pour l'image et le bouton de sauvegarde
        self.image_save_layout = QHBoxLayout()
        self.image_save_layout.setAlignment(Qt.AlignCenter)

        # Label pour l'image
        self.image_label = QLabel('No Image Selected', self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet('color: white; border: 2px solid white; padding: 10px;')
        self.image_save_layout.addWidget(self.image_label)

        # Bouton pour enregestrer l'image
        self.save_button = QPushButton('Save', self)
        self.save_button.setStyleSheet(
            'background-color: grey; color: white; border: 2px solid white; padding: 10px;'
        )
        self.save_button.hide()
        self.image_save_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_image)

        self.layout.addLayout(self.image_save_layout)

        # Bouton pour sélectionner l'image
        self.select_image_button = QPushButton('Select Image', self)
        self.select_image_button.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 10px; min-width: 200px;'
        )
        self.layout.addWidget(self.select_image_button)
        self.select_image_button.clicked.connect(self.open_image_dialog)

        # Champ pour saisir le token
        self.token_input = QLineEdit(self)
        self.token_input.setPlaceholderText("Enter your token ")
        self.token_input.setStyleSheet('color: black; background-color: white; padding: 10px; border: 2px solid black;')
        self.layout.addWidget(self.token_input)

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
        self.process_button = QPushButton('Start', self)
        self.process_button.setStyleSheet(
            'background-color: #555; color: white; border: 2px solid white; padding: 10px; min-width: 200px;'
        )
        self.layout.addWidget(self.process_button)
        self.process_button.clicked.connect(self.start_processing)

        # Configuration de la fenêtre principale
        self.setLayout(self.layout)
        self.setWindowTitle('Image Selector and Choices')
        self.setStyleSheet('background-color: white;')
        self.setFixedSize(400, 550)

        # Variable pour stocker le chemin de l'image sélectionnée
        self.image_path = None

    def open_image_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Images (*.png *.xpm *.jpg)',
                                                   options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
            self.image_path = file_name

    def client(self, image_path, modifications, token):
        mods = ["rotate_left", "rotate_right", "inverse", "b&w", "grayscale"]

        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        adresse = "http://192.168.0.23:5000/modification"
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
        if response.status_code == 400:
            error_message = response.json().get("message", "Erreur inconnue")
            return {"error": True, "message": error_message}
        
        decoded_image = base64.b64decode(response.text)
        return {"error": False, "image": decoded_image}
    

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

    def save_image(self):
        if self.image_label.pixmap() is not None:
            # Ouvrir un dialogue pour choisir l'emplacement et le nom du fichier avec plusieurs extensions
            options = QFileDialog.Options()
            file_name, selected_filter = QFileDialog.getSaveFileName(
                self,
                "Save Image As",
                "",
                "PNG Files (*.png);;JPEG Files (*.jpg);;XPM Files (*.xpm);;All Files (*)",
                options=options
            )

            if file_name:
                # Récupérer l'extension en fonction du filtre sélectionné
                if selected_filter == "PNG Files (*.png)":
                    extension = "PNG"
                elif selected_filter == "JPEG Files (*.jpg)":
                    extension = "JPG"
                elif selected_filter == "XPM Files (*.xpm)":
                    extension = "XPM"
                else:
                    extension = "PNG"  # Par défaut

                try:
                    # Enregistrer l'image avec l'extension sélectionnée
                    self.image_label.pixmap().save(file_name, extension)
                except Exception as e:
                    QMessageBox.critical(self, 'Error', f'Failed to save image: {str(e)}')
        else:
            QMessageBox.warning(self, 'Warning', 'No image to save.')

    def start_processing(self):
        if self.image_path is None:
            QMessageBox.warning(self, 'Warning', 'Please select an image before sending to the server.')
            return

        token = self.token_input.text()
        if not token:
            self.token_input.setStyleSheet(
                'color: red; background-color: white; padding: 10px; border: 2px solid white;')
            return

        selected_items = self.list_widget.selectedItems()
        modifications = [item.text() for item in selected_items]

        if not modifications:
            QMessageBox.warning(self, 'Warning',
                                'Please select at least one modification before sending to the server.')
            return

        try:
            response = self.client(self.image_path, modifications, token)

            if response["error"]:
                QMessageBox.critical(self, 'Error', response["message"])
            else:
                decoded_image = response["image"]
                pixmap = QPixmap()
                pixmap.loadFromData(decoded_image)
                self.image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
                self.save_button.show()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to send data to server: {str(e)}')


app = QApplication(sys.argv)
window = ImageSelector()
window.show()
sys.exit(app.exec_())
