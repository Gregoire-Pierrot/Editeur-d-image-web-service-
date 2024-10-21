/**
 * File ImageHandler.java
 * @author Tiago Feitosa
 * @version 1.1
 */

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.geom.AffineTransform;
import java.awt.image.BufferedImage;
import java.io.*;
import java.net.Socket;
import java.util.Base64;

/**
 * Enum for Instructions
 */
enum Instruction {
    ROTATE_LEFT,
    ROTATE_RIGHT,
    INVERT_HORIZONTAL,
    INVERT_VERTICAL,
    BLACK_WHITE,
}

/**
 * Enum for Orientation
 */
enum Orientation {
    HORIZONTAL,
    VERTICAL,
}

/**
 * Class to handle image processing
 */
public class ImageHandler {

    private String imageBase64;
    private String processedImage;

    /**
     * Constructor
     * @param imageBase64 - String
     */
    public ImageHandler(String imageBase64) {
        this.imageBase64 = imageBase64;
        this.processedImage = null;
    }

    /**
     * Méthode publique pour récupérer l'image modifiée
     * Public Mehtod to return the modified image
     * @param instruction - Enum
     * @return string - Modified image
     */
    public String getModifiedImage(Instruction instruction) {
        processedImage = processImage(imageBase64, instruction);
        return processedImage;
    }

    /**
     * Method to process image
     * Reçoit les images au format String, les met en mémoire tampon, les traite, puis renvoie leur format à String
     * Receives images in String format, buffers it, processes it, then returns its format back to String
     * @param imageBase64 - String
     * @param instruction - enum
     * @return String
     */
    private String processImage(String imageBase64, Instruction instruction) {
        try {
            byte[] decodedBytes = Base64.getDecoder().decode(imageBase64);
            ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(decodedBytes);
            BufferedImage image = ImageIO.read(byteArrayInputStream);
            byteArrayInputStream.close();
            BufferedImage processedImage = null;
            switch (instruction) {
                case ROTATE_LEFT -> processedImage = rotateImage(image, -90);
                case ROTATE_RIGHT -> processedImage = rotateImage(image, 90);
                case INVERT_HORIZONTAL -> processedImage = invertImage(image, Orientation.HORIZONTAL);
                case INVERT_VERTICAL -> processedImage = invertImage(image, Orientation.VERTICAL);
                case BLACK_WHITE -> processedImage = desaturateImage(image);
                default -> System.out.println("Unknown Instruction.");
            }
            ByteArrayOutputStream output = new ByteArrayOutputStream();
            ImageIO.write(processedImage, "jpg", output);
            String encodedModifiedImage = Base64.getEncoder().encodeToString(output.toByteArray());
            System.out.println("Image processed successfully.");
            return encodedModifiedImage;
        } catch (IOException e) {
            System.out.println("Error processing the image: " + e.getMessage());
            return null;
        }
    }



    /**
     * Method to turn image black and white
     * @param original - original ofrmat of Buffered Image
     * @return - returns modified Buffered Image
     */
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

    /**
     * Method to rotate image, use positive values to turn it clockwise, negative values for counterclockwise
     * @param img
     * @param angle - double
     * @return
     */
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

    /**
     * Method to invert image, use enum to choose orientation
     * @param img
     * @param orientation - enum
     * @return
     */
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

    /*private void sendImageToClient(String processedImagePath) throws IOException {
        File imageFile = new File(processedImagePath);
        byte[] imageBytes = new byte[(int) imageFile.length()];
        FileInputStream fileInputStream = new FileInputStream(imageFile);
        BufferedInputStream bufferedInputStream = new BufferedInputStream(fileInputStream);
        bufferedInputStream.read(imageBytes, 0, imageBytes.length);

        OutputStream outputStream = clientSocket.getOutputStream();
        outputStream.write(imageBytes, 0, imageBytes.length);
        outputStream.flush();
        bufferedInputStream.close();
    }*/


    // If processing is successful, a processed image file will be created on the main folder named: output_image.jpg
    // Si le traitement réussit, un fichier image traité sera créé dans le dossier principal nommé : output_image.jpg

    /**
     * Process image and save to main folder for future use
     * @param imageBase64
     * @param instruction
     * @return boolean for successful operation
     */
    /*private boolean processAndSave(String imageBase64, Instruction instruction) {

        try {
            byte[] decodedBytes = Base64.getDecoder().decode(imageBase64);
            ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(decodedBytes);
            BufferedImage image = ImageIO.read(byteArrayInputStream);
            byteArrayInputStream.close();

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
    }*/

}
