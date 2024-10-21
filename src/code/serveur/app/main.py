from app import app # importation de l'application flask
import views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')