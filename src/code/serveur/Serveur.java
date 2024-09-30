import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

public final class Serveur {
    private final static int MAX_CLIENT = 20;

    private static Serveur instance;
    private final String ip;
    private final int port;

    private int nbClients;

    private Executor executor;

    private static ServeurHandler[] serveurHandlers = new ServeurHandler[MAX_CLIENT];
    private static double[] tokens = new double[MAX_CLIENT];

    private Serveur(String ip, int port){
        this.ip = ip;
        this.port = port;
        nbClients = 0;
    }

    public static Serveur getInstance(String ip, int port){
        if (instance == null)
            instance = new Serveur(ip, port);
        return instance;
    }

    public static void main(String[] args) {
        if (args.length == 2){
            try {
                Serveur serveur = getInstance(args[0], Integer.parseInt(args[1]));
                serveur.serveurStart();
            } catch (Exception e) {
                System.out.println("Error on ip or port");
            }
        }
        else {
            System.out.println("Error Synthaxe : java Serveur ip port");
        }
    }

    public void serveurStart() throws IOException {
        ServerSocket serveur = new ServerSocket(this.port, 1, InetAddress.getByName(ip));
        System.out.println("Serveur up !\n------------------");
        System.out.println("ip : " + ip + ", port : " + port);
        System.out.println("Waiting for clients ...\n");

        while (true) {
            if (nbClients == MAX_CLIENT){
                break;
            }
            Socket client = serveur.accept();
            nbClients++;
            ServeurHandler handler = new ServeurHandler(client);
            serveurHandlers[nbClients - 1] = handler;
            this.executor = Executors.newCachedThreadPool();
            executor.execute(handler);
        }
    }

    public void setToken(double token){
        tokens[nbClients] = token;
    }

    public static void echoMessage(String message){
        System.out.println(message);
    }
}