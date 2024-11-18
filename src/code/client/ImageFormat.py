import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Fonction pour vérifier les formats d'image acceptés
def verifier_format_image(fichier_image):
    formats_acceptes = ['JPEG', 'PNG', 'BMP']
    try:
        with Image.open(fichier_image) as img:
            if img.format not in formats_acceptes:
                messagebox.showerror("Erreur", f"Format d'image non supporté : {img.format}")
                return False
            else:
                print(f"Format accepté : {img.format}")
                return True
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'ouverture de l'image : {e}")
        return False

# Fonction pour sélectionner une image et l'afficher dans l'interface
def selectionner_image():
    fichier_image = filedialog.askopenfilename(
        title="Sélectionner une image",
        filetypes=[("Fichiers image", "*.jpg;*.png;*.bmp")]
    )
    
    if fichier_image:
        # Vérification du format de l'image
        if verifier_format_image(fichier_image):
            # Afficher l'image sélectionnée
            img = Image.open(fichier_image)
            img.thumbnail((300, 300))  # Redimensionner pour l'interface
            img_tk = ImageTk.PhotoImage(img)
            
            label_image.config(image=img_tk)
            label_image.image = img_tk  # Nécessaire pour maintenir la référence à l'image
            label_message.config(text=f"Image sélectionnée : {os.path.basename(fichier_image)}")
            
            # Sauvegarder le chemin de l'image sélectionnée pour une utilisation ultérieure
            app.fichier_image = fichier_image

# Fonction pour simuler l'envoi de l'image
def envoyer_image():
    if hasattr(app, 'fichier_image'):
        instruction = "rotation_gauche"  # Remplacer par la vraie instruction
        print(f"Envoi de l'image avec l'instruction '{instruction}'...")
        # Ici si c est possible d'ajouter le code pour traiter l'image ou l'envoyer au serveur
        messagebox.showinfo("Succès", "Image envoyée avec succès ! (Simulation)")
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une image d'abord.")

# Création de l'interface utilisateur avec Tkinter
app = tk.Tk()
app.title("Client de Modification d'Image")
app.geometry("400x400")

# Bouton pour sélectionner une image
btn_select_image = tk.Button(app, text="Sélectionner une image", command=selectionner_image)
btn_select_image.pack(pady=10)

# Label pour afficher les informations sur l'image
label_message = tk.Label(app, text="Aucune image sélectionnée")
label_message.pack(pady=5)

# Label pour afficher l'image sélectionnée
label_image = tk.Label(app)
label_image.pack(pady=10)

# Bouton pour envoyer l'image
btn_envoyer_image = tk.Button(app, text="Envoyer l'image", command=envoyer_image)
btn_envoyer_image.pack(pady=10)

# Lancement de l'application
app.mainloop()
