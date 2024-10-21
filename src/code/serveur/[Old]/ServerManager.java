import java.io.PrintWriter;

public class ServerManager {

    public static boolean isInstruction(String instruction) {
        switch (instruction) {
            case "ROTATE_LEFT":
                return true;
            case "ROTATE_RIGHT":
                return true;
            case "INVERT_HORIZONTAL":
                return true;
            case "INVERT_VERTICAL":
                return true;
            case "BLACK_WHITE":
                return true;
            default:
                return false;
        }
    }

    public static Instruction stringToInstruction(String instruction) {
        switch (instruction) {
            case "ROTATE_LEFT":
                return Instruction.ROTATE_LEFT;
            case "ROTATE_RIGHT":
                return Instruction.ROTATE_RIGHT;
            case "INVERT_HORIZONTAL":
                return Instruction.INVERT_HORIZONTAL;
            case "INVERT_VERTICAL":
                return Instruction.INVERT_VERTICAL;
            case "BLACK_WHITE":
                return Instruction.BLACK_WHITE;
            default:
                return null;
        }
    }

    public static boolean transformImage(String insctructionString, String token){
        Instruction instruction = stringToInstruction(insctructionString);
        ImageHandler imageHandler = new ImageHandler();
        return false;
    }

    public static boolean isImage(String image) {
        return true;
    }
}
