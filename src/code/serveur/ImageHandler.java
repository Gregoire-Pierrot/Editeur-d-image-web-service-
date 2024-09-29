import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.geom.AffineTransform;
import java.awt.image.BufferedImage;
import java.io.*;
import java.net.Socket;
import java.util.Base64;

enum Orientation {
    HORIZONTAL,
    VERTICAL,
}
enum Instruction {
    ROTATE_LEFT,
    ROTATE_RIGHT,
    INVERT_HORIZONTAL,
    INVERT_VERTICAL,
    BLACK_WHITE,
}

public class ImageHandler {

    private final Socket clientSocket;
    private final PrintWriter out;

    public ImageHandler(Socket clientSocket, PrintWriter out) {
        this.clientSocket = clientSocket;
        this.out = out;
    }

    // If processing is successful, a processed image file will be created on the main folder named: output_image.jpg
    private boolean processImage(String imageBase64, Instruction instruction) {

        try {
            byte[] decodedBytes = Base64.getDecoder().decode(imageBase64);
            ByteArrayInputStream bis = new ByteArrayInputStream(decodedBytes);
            BufferedImage image = ImageIO.read(bis);
            bis.close();

            BufferedImage processedImage = null;
            switch (instruction) {
                case ROTATE_LEFT -> processedImage = rotateImage(image, -90);
                case ROTATE_RIGHT -> processedImage = rotateImage(image, 90);
                case INVERT_HORIZONTAL -> processedImage = invertImage(image, Orientation.HORIZONTAL);
                case INVERT_VERTICAL -> processedImage = invertImage(image, Orientation.VERTICAL);
                case BLACK_WHITE -> processedImage = desaturateImage(image);
                default -> out.println("Unknown Instruction.");
            }

            String outputPath = "output_image.jpg";
            File outputImage = new File(outputPath);
            ImageIO.write(processedImage, "jpg", outputImage);

            ByteArrayOutputStream output = new ByteArrayOutputStream();
            ImageIO.write(processedImage, "jpg", output);
            String encodedModifiedImage = Base64.getEncoder().encodeToString(output.toByteArray());
            out.println("Image saved to " + outputPath);

            return true;

        } catch (IOException e) {
            out.println("Error saving the image " + e.getMessage());
            return false;
        }
    }

    private BufferedImage desaturateImage(BufferedImage original) {
        int width = original.getWidth();
        int height = original.getHeight();
        BufferedImage desaturatedImage = new BufferedImage(width, height, original.getType());
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                Color color = new Color(original.getRGB(x, y));
                int red = color.getRed();
                int green = color.getGreen();
                int blue = color.getBlue();
                int gray = (red + green + blue) / 3;
                Color grayColor = new Color(gray, gray, gray, color.getAlpha());
                desaturatedImage.setRGB(x, y, grayColor.getRGB());
            }
        }
        return desaturatedImage;
    }

    private BufferedImage rotateImage(BufferedImage img, double angle) {
        int width = img.getWidth();
        int height = img.getHeight();
//        BufferedImage rotatedImage = new BufferedImage(height, width, img.getType());
        @SuppressWarnings("SuspiciousNameCombination")
        BufferedImage rotatedImage = new BufferedImage(height, width, img.getType());
        Graphics2D g2d = rotatedImage.createGraphics();
        AffineTransform at = new AffineTransform();
        at.translate((double) (height - width) / 2, (double) (width - height) / 2);
        at.rotate(Math.toRadians(angle), (double) width / 2, (double) height / 2);
        g2d.setTransform(at);
        g2d.drawImage(img, 0, 0, null);
        g2d.dispose();
        return rotatedImage;
    }
    private BufferedImage invertImage(BufferedImage img,  Orientation orientation) {
        int width = img.getWidth();
        int height = img.getHeight();
        BufferedImage invertedImage = new BufferedImage(width, height, img.getType());
        switch (orientation) {
            case HORIZONTAL -> {
                for (int y = 0; y < height; y++) {
                    for (int x = 0; x < width; x++) {
                        int pixel = img.getRGB(x, y);
                        invertedImage.setRGB(width - 1 - x, y, pixel);
                    }
                }
            }
            case VERTICAL -> {
                for (int y = 0; y < height; y++) {
                    for (int x = 0; x < width; x++) {
                        invertedImage.setRGB(x, height - 1 - y, img.getRGB(x, y));
                    }
                }
            }
            default -> out.println("Unknown Orientation");
        }
        return invertedImage;
    }

    private void sendImageToClient(String processedImagePath) throws IOException {
        File imageFile = new File(processedImagePath);
        byte[] imageBytes = new byte[(int) imageFile.length()];
        FileInputStream fileInputStream = new FileInputStream(imageFile);
        BufferedInputStream bufferedInputStream = new BufferedInputStream(fileInputStream);
        bufferedInputStream.read(imageBytes, 0, imageBytes.length);

        OutputStream outputStream = clientSocket.getOutputStream();
        outputStream.write(imageBytes, 0, imageBytes.length);
        outputStream.flush();
        bufferedInputStream.close();
    }

}
