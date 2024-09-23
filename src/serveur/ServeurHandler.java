package code.serveur;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Random;

public class ServeurHandler extends Thread{

    private Socket client;

    private Random random = new Random();
    private final double token = random.nextDouble(Math.pow(2, 32));

    public ServeurHandler(Socket client){
        this.client = client;
    }

    public void run(){
        try {
            InputStream input = this.client.getInputStream();
            OutputStream output = this.client.getOutputStream();
    
            byte[] buffer = new byte[8196];
            int bytes = 0;

            if ((bytes = input.read(buffer)) != -1) {
                Serveur.echoMessage("\nNew connection from " + this.client.getInetAddress() + "\n");

                output.write(new String("Connected. Here your token : " + token).getBytes());
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