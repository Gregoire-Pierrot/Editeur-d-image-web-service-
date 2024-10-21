import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Objects;

public class ServeurHandler extends Thread{

    private Socket client;
    private String token = TokenGenerator.generateToken();

    public ServeurHandler(Socket client){
        this.client = client;
    }

    public void run(){
        try {
            InputStream input = this.client.getInputStream();
            OutputStream output = this.client.getOutputStream();
    
            byte[] buffer = new byte[8196];
            int bytes = 0;

            Serveur.echoMessage("\nNew connection from " + this.client.getInetAddress() + "\n");

            if ((bytes = input.read(buffer)) != -1) {
                output.write(token.getBytes());
            }
    
            while ((bytes = input.read(buffer)) != -1) {
                String message = new String(buffer, 0, bytes);
                Serveur.echoMessage(message);
                String[] messageParsed = message.split(" ");
                if (messageParsed[0].compareTo(token) != 0) {
                    if (ServerManager.isInstruction(messageParsed[1])) {
                        if(ServerManager.isImage(messageParsed[2])) {
                            output.write(new String("Valide").getBytes());
                            // Lire les données de l'image
                            byte[] image_byte = messageParsed[2].getBytes(StandardCharsets.UTF_8);
                            ByteBuffer imageBuffer = ByteBuffer.wrap(image_byte);
                            imageBuffer.flip();
                            // Sauvegarder les données en tant que fichier PNG
                            try (FileOutputStream fos = new FileOutputStream("./ressources/serveur/" + token + ".png")) {
                                fos.write(imageBuffer.array());
                            }
                            if (ServerManager.transformImage(messageParsed[1], token)){
                                byte[] decodedBytes = Base64.getDecoder().decode("./ressources/serveur/" + token + ".png");
                                output.write(decodedBytes);
                                /* TODO: Remove images client */
                            }
                            else {
                                output.write(new String("Error on transformation, try again.").getBytes());
                            }
                        }
                        else {
                            output.write(new String("Invalide image").getBytes());
                        }
                    }
                    else {
                        output.write(new String("Invalide instruction").getBytes());
                    }
                }
                else {
                    client.close();
                    break;
                }
            }
        } catch (IOException e) {
            System.out.println("Error on input or output");
        }
    }

    public Socket getClient(){ return this.client; }
}