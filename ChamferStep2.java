import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class ChamferStep2 {
    public static void main(String[] args) {
        try {
            // 1. 讀取 X 軸與 Y 軸的掃描結果圖
            File fileX = new File("output_X.png");
            File fileY = new File("output_Y.png");
            
            if (!fileX.exists() || !fileY.exists()) {
                System.out.println("❌ 錯誤：找不到 output_X.png 或 output_Y.png，請先執行掃描程式。");
                return;
            }

            BufferedImage imgX = ImageIO.read(fileX);
            BufferedImage imgY = ImageIO.read(fileY);
            int w = imgX.getWidth();
            int h = imgX.getHeight();

            // 2. 建立一張新的空白圖，準備存合成結果
            BufferedImage finalImg = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);

            System.out.println("正在合併 X 軸與 Y 軸掃描結果...");

            for (int r = 0; r < h; r++) {
                for (int c = 0; c < w; c++) {
                    // 取得 X 與 Y 圖的亮度 (代表距離)
                    int valX = new Color(imgX.getRGB(c, r)).getRed();
                    int valY = new Color(imgY.getRGB(c, r)).getRed();

                    // 合成邏輯：取兩者中較小的距離 (這就是標準的 Chamfer 邏輯)
                    // 這樣會讓生成的圖片看起來最接近原本的距離變換
                    int finalVal = Math.min(valX, valY);

                    // 設定顏色 (維持灰階，接近原圖感)
                    Color newColor = new Color(finalVal, finalVal, finalVal);
                    finalImg.setRGB(c, r, newColor.getRGB());
                }
            }

            // 3. 儲存最終生成的圖
            ImageIO.write(finalImg, "png", new File("final_combined.png"));
            System.out.println("✅ 合成完成！請查看 final_combined.png");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}