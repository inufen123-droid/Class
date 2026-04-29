
import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class ChamferStep1 {
    static final double INF = 1e6;

    public static void main(String[] args) {
        try {
            File inputFile = new File("main.png");
            BufferedImage img = ImageIO.read(inputFile);
            int w = img.getWidth();
            int h = img.getHeight();

            // 初始化距離矩陣
            double[][] distX = new double[h][w];
            double[][] distY = new double[h][w];

            for (int r = 0; r < h; r++) {
                for (int c = 0; c < w; c++) {
                    int gray = getGray(img.getRGB(c, r));
                    double val = (gray < 128) ? 0 : INF;
                    distX[r][c] = val;
                    distY[r][c] = val;
                }
            }

            // --- 1. X 軸掃描 (左右方向) ---
            // Forward (左到右)
            for (int r = 0; r < h; r++) {
                for (int c = 1; c < w; c++) {
                    distX[r][c] = Math.min(distX[r][c], distX[r][c - 1] + 1);
                }
            }
            // Backward (右到左)
            for (int r = 0; r < h; r++) {
                for (int c = w - 2; c >= 0; c--) {
                    distX[r][c] = Math.min(distX[r][c], distX[r][c + 1] + 1);
                }
            }

            // --- 2. Y 軸掃描 (上下方向) ---
            // Forward (上到下)
            for (int c = 0; c < w; c++) {
                for (int r = 1; r < h; r++) {
                    distY[r][c] = Math.min(distY[r][c], distY[r - 1][c] + 1);
                }
            }
            // Backward (下到上)
            for (int c = 0; c < w; c++) {
                for (int r = h - 2; r >= 0; r--) {
                    distY[r][c] = Math.min(distY[r][c], distY[r + 1][c] + 1);
                }
            }

            // --- 3. 生成圖片 ---
            saveDistanceImage(distX, w, h, "output_X.png");
            saveDistanceImage(distY, w, h, "output_Y.png");

            System.out.println("✅ 成功！已生成兩張圖片：");
            System.out.println("1. output_X.png (水平距離地圖)");
            System.out.println("2. output_Y.png (垂直距離地圖)");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static int getGray(int rgb) {
        Color c = new Color(rgb);
        return (c.getRed() + c.getGreen() + c.getBlue()) / 3;
    }

    private static void saveDistanceImage(double[][] dist, int w, int h, String fileName) throws Exception {
        BufferedImage out = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);
        // 尋找最大值進行正規化 (讓圖片看得清楚)
        double max = 0;
        for (int r = 0; r < h; r++) {
            for (int c = 0; c < w; c++) {
                if (dist[r][c] < INF && dist[r][c] > max) max = dist[r][c];
            }
        }
        if (max == 0) max = 1;

        for (int r = 0; r < h; r++) {
            for (int c = 0; c < w; c++) {
                int grayVal = (int) (dist[r][c] / max * 255);
                grayVal = Math.min(255, grayVal);
                out.setRGB(c, r, new Color(grayVal, grayVal, grayVal).getRGB());
            }
        }
        ImageIO.write(out, "png", new File(fileName));
    }
}