from app import app
import views

if __name__ == '__main__':
    #https (ne marche pas, le serveur se lance mais impossible d'y acceder)
    #app.run(host='0.0.0.0', port='5000', ssl_context=("cert.pem", "key.pem"), debug=True)
    
    #http
    app.run(host='0.0.0.0', port='5000')