import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class ServeurHandler extends Thread{

    private Socket client;

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
                output.write(new String("Connected.").getBytes());
            }
    
            while ((bytes = input.read(buffer)) != -1) {
                String message = new String(buffer, 0, bytes);
                Serveur.echoMessage(message);
            }
        } catch (IOException e) {
            System.out.println("Error on input or output");
        }
    }

    public Socket getClient(){ return this.client; }
}