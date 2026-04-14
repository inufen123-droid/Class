import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] scores = {70, 80, 90};
        int sum = 0;

        // 使用迴圈加總
        for (int score : scores) {
            sum += score;
        }

        // 計算平均（轉為 double 以保持精確度）
        double average = (double) sum / scores.length;
        int maxNum = findMax(scores);
        int minNum = findMin(scores);
       
        System.out.println("1.The average score is: " + average);
        System.out.println("2.The Max is: " + maxNum);
        System.out.println("10.The Min is: " + minNum);

        System.out.println("3.加5之前:"+Arrays.toString(scores));

        addBonus(scores);

        int add_sum=0;
        for (int score : scores) {
            add_sum += score;
        }
       
        System.out.println("  加5之後:"+Arrays.toString(scores));//第3題

        // --- 第 7 題測試：傳回陣列總和 ---
        int[] demoScores = {70, 80, 90};
        int total = sum(demoScores);
        System.out.println("7.陣列總和: " + total);//1~3 and 7題

        Student tom = new Student("Tom", 85);
        System.out.println("4."+tom.name + ": " + tom.score); 
        System.out.println(); 
          
        Student[] students = {
            new Student("Alice", 55),
            new Student("Bob", 75),
            new Student("Charlie", 45),
            tom
        };

        // --- 第 6 題：統計及格人數 ---
        int passCount = 0;
        for (Student s : students) {
            if (s.score >= 60) {
                passCount++;
            }
        }
        System.out.println("6. 及格 (>=60) 的學生人數: " + passCount);
        System.out.println();//6.

        // --- 第 8 題：使用循環列印所有學生姓名與分數 ---
        System.out.println("8. 學生名單列表：");
        for (Student s : students) {
            System.out.println("姓名: " + s.name + ", 分數: " + s.score);
        }
        System.out.println();
        
        System.out.println("加分處理中...");
        updateScore(students[1], 80); // 更新 Bob 的分數為 80(第九題)
        for (Student s : students) {
            curve(s); // 檢查是否需要加 10 分
        }

        System.out.println("成績更新後的學生名單列表：");
        for (Student s : students) {
            System.out.println("姓名: " + s.name + ", 分數: " + s.score);
        }
        System.out.println();

        
    }//主程式
        
    
    
///////////////////////////////////////////////////////////////////////////////////////////
    public static int findMax(int[] arr) {
        // 1. 防呆機制：確保陣列不是空的
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("The array cannot be empty.");
        }

        // 2. 初始化：假設第一個元素就是最大值
        int max = arr[0];

        // 3. 走訪：從第二個元素開始比較 (索引 1)
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i]; // 發現更大的數，更新 max
            }
        }

        return max;
    }

    public static void addBonus(int[] scores) {
        for (int i = 0; i < scores.length; i++) {
            // 將原本的值取出加 5 後再存回去
            scores[i] = scores[i] + 5;
            
            // 也可以簡寫成：
            // scores[i] += 5;
        }
    }

    public static void curve(Student s) {
        if (s.score < 60) {
            s.score += 10;
        }
    }

    // 第 7 題：計算並傳回整數陣列總和
    public static int sum(int[] arr) {
        int total = 0;
        for (int num : arr) {
            total += num;
        }
        return total;
    }

    // 第 9 題：更新學生的分數
    public static void updateScore(Student s, int newScore) {
        s.score = newScore;
    }
    //第10題:找最小
    public static int findMin(int[] arr) {
        // 防呆：確保陣列不是空的
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("陣列不能為空");
        }

        // 1. 初始化：假設第一個元素就是最小值
        int min = arr[0];

        // 2. 走訪：從第二個元素開始比較
        for (int i = 1; i < arr.length; i++) {
            // 如果當前元素比我們紀錄的 min 還要小
            if (arr[i] < min) {
                min = arr[i]; // 更新最小值紀錄
            }
        }

        // 3. 回傳結果
        return min;
    }    
}

class Student {
    String name;
    int score;

    // 建構子 (Constructor)，用來初始化物件屬性
    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
}   