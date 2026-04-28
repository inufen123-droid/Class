class BasicProbability {
    public void displayExample() {
        System.out.println("--- 1. 機率的定義  ---");
        System.out.println("定義：表示某件事情發生的可能性 ");
        System.out.println("公式：P(A) = 事件A發生的個數 / 全部可能情況 ");
    }
}

class SampleSpace{
    public void displayExample() {
        System.out.println("\n--- 2. 樣本空間  ---");
        System.out.println("定義：S=所有可能結果的集合 ");
    }
}

class Event{
    public void displayExample() {
        System.out.println("\n--- 3. 事件  ---");
        System.out.println("定義：A=我們關心的事件 ");
    }
}

class formula{
    private double nA = 30;
    private double nS = 100; 

    public void displayExample() {
        System.out.println("\n--- 4. 基本公式  ---");
        System.out.println(" P(A)=n(A)/n(S) ");

        double Probability = nA/nS;
        System.out.println("範例: A=30,S=100;P(A)= "+ Probability   );
    }
}

// 5. 補事件 (Page 6)
class ComplementEvent {
    public void displayExample() {
        System.out.println("\n--- 5. 補事件 ---");
        System.out.println("公式：P(A^C) = 1 - P(A) ");
        double pA = 0.3;
        System.out.println("範例：不是建中的機率 = 1 - " + pA + " = " + (1 - pA) );
    }
}

// 6. 聯集 OR (Page 7)
class UnionProbability {
    public void displayExample() {
        System.out.println("\n--- 6. 聯集  ---");
        System.out.println("公式：P(A ∪ B) = P(A) + P(B) - P(A ∩ B) ");
        // 使用第 7 頁範例數值 [cite: 46, 47, 48]
        double pA = 0.53, pB = 0.45, pIntersection = 0.20;
        double result = pA + pB - pIntersection;
        System.out.println("範例結果：0.53 + 0.45 - 0.20 = " + String.format("%.2f", result) );
    }
}

// 7. 交集 AND (Page 8)
class IntersectionProbability {
    public void displayExample() {
        System.out.println("\n--- 7. 交集 (Page 8) ---");
        System.out.println("公式：P(A ∩ B) = P(A)P(B|A) ");
        // 使用第 8 頁範例數值 [cite: 57, 58]
        double pA = 0.60, pBgivenA = 0.35;
        double result = pA * pBgivenA;
        System.out.println("範例結果：0.60 * 0.35 = " + String.format("%.2f", result) );
    }
}

// 8. 條件機率 (Page 9)
class ConditionalProbability {
    public void displayExample() {
        System.out.println("\n--- 8. 條件機率 ---");
        System.out.println("定義：已知 B 發生，A 的機率 ");
        System.out.println("公式：P(A|B) = P(A ∩ B) / P(B) ");
        // 使用第 9 頁範例數值 [cite: 69, 70]
        double pB = 0.65, pIntersection = 0.30;
        System.out.println("範例結果：0.30 / 0.65 ≈ " + String.format("%.2f", pIntersection / pB) );
    }
}

// 9. 獨立事件 (Page 10)
class IndependentEvent {
    public void displayExample() {
        System.out.println("\n--- 9. 獨立事件  ---");
        System.out.println("定義：若 A、B 獨立，則 P(A ∩ B) = P(A)P(B)");
        // 使用第 10 頁範例數值 [cite: 80, 81, 85]
        double pA = 0.60, pB = 0.45, pIntersection = 0.27;
        System.out.println("驗證：0.60 * 0.45 = " + (pA * pB) + " (等於 " + pIntersection + " 為獨立) ");
    }
}

// 10. 貝氏定理 (Page 11)
class BayesTheorem {
    public void displayExample() {
        System.out.println("\n--- 10. 貝氏定理 ---");
        System.out.println("公式：P(A|B) = P(B|A)P(A) / P(B) ");
        System.out.println("用途：已知結果，反推原因 ");
    }
}

// 11. 全機率公式 (Page 12)
class TotalProbability {
    public void displayExample() {
        System.out.println("\n--- 11. 全機率公式 ---");
        System.out.println("公式：P(A) = Σ P(A|Bi)P(Bi) ");
    }
}

class SchoolExample {
    // 定義參數 (nA, nS 的具體化)
    private double J = 30; // 建中學生人數 (nA_J)
    private double B = 20; // 北一女學生人數 (nA_B)
    private double N = 100; // 總人數 (nS)

    public void displayExample() {
        System.out.println("\n--- 12. 學校例子 ---");
        System.out.println("情境：交大中學生的來源比例");
        System.out.println("輸入參數：");
        System.out.println("  J (建中人數) = " + (int)J +"  B (北一女人數) = " + (int)B +"  N (學校總人數) = " + (int)N);
        
        // 1. 計算抽到建中學生的機率
        double pJ = J / N;
        System.out.println(" \n P(建中) = J / N");
        System.out.println("  結果：" + (int)J + " / " + (int)N + " = " + pJ);

        // 2. 計算抽到北一女學生的機率
        double pB = B / N;
        System.out.println("  \nP(北一女) = B / N");
        System.out.println("  結果：" + (int)B + " / " + (int)N + " = " + pB);

        // 3. 互斥事件聯集 (抽到建中或北一女)
        // 因為一個學生不能同時是建中又是北一女，所以是互斥事件
    }   
}

class schoool_2{
    private double J = 30; // 建中學生人數 (nA_J)
    private double B = 20; // 北一女學生人數 (nA_B)
    private double N = 100; // 總人數 (nS)

    public void displayExample() {
        double pUnion = (J + B) / N;
        System.out.println("\n--- 13. 建中或北一女 ---");    
        System.out.println("[計算 ：互斥聯集]");
        System.out.println("  說明：學生不能同時屬於兩校，故為互斥事件");
        System.out.println("  P(建中 ∪ 北一女) = (J + B) / N");
        System.out.println("  結果：(" + (int)J + " + " + (int)B + ") / " + (int)N + " = " + pUnion);
        System.out.println("---------------------------------");
    }
}

// 主程式執行區
public class ProbabilityAssignment {
    public static void main(String[] args) {
        // 為講義的每一部分建立獨立的類別物件 
        BasicProbability page2 = new BasicProbability();
        SampleSpace page3 = new SampleSpace();
        Event page4 = new Event();
        formula page5 =new formula();
        ComplementEvent page6 = new ComplementEvent();
        UnionProbability page7 = new UnionProbability();
        IntersectionProbability page8 = new IntersectionProbability();
        ConditionalProbability page9 = new ConditionalProbability();
        IndependentEvent page10 = new IndependentEvent();
        BayesTheorem page11 = new BayesTheorem();
        TotalProbability page12 = new TotalProbability();
        SchoolExample page13 = new SchoolExample();
        schoool_2 page14 = new schoool_2();

        // 呼叫並顯示結果
        page2.displayExample();
        page3.displayExample();
        page4.displayExample();
        page5.displayExample();
        page6.displayExample();
        page7.displayExample();
        page8.displayExample();
        page9.displayExample();
        page10.displayExample();
        page11.displayExample();
        page12.displayExample();
        page13.displayExample();
        page14.displayExample();
    }
}
