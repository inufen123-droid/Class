#include <bits/stdc++.h>
using namespace std;

struct Person {
    double x, y;
    int label; // 0=A, 1=B, 2=C
};

struct Neighbor {
    double distance;
    int label;
    double x, y;
};

// 歐幾里得距離
double dist(Person a, Person b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

// KNN 回傳選到的鄰居
int knn_with_neighbors(vector<Person>& people, Person& me, int k, bool weighted,
                       vector<Neighbor>& selected_neighbors) {

    vector<Neighbor> all;

    for (int i = 0; i < people.size(); i++) {
        double d = dist(people[i], me);

        Neighbor n;
        n.distance = d;
        n.label = people[i].label;
        n.x = people[i].x;
        n.y = people[i].y;

        all.push_back(n);
    }

    sort(all.begin(), all.end(), [](Neighbor a, Neighbor b) {
        return a.distance < b.distance;
    });

    map<int, double> vote;
    selected_neighbors.clear();

    for (int i = 0; i < k; i++) {
        selected_neighbors.push_back(all[i]);
        double d = all[i].distance;
        int label = all[i].label;
        if (weighted) {
            double w = (d == 0) ? 1e9 : 1.0 / (d * d);  // 距離平方加權
            vote[label] += w;
        } else {
            vote[label] += 1;
        }
    }

    int best = -1;
    double mx = -1;
    for (auto it = vote.begin(); it != vote.end(); it++) {
        if (it->second > mx) {
            mx = it->second;
            best = it->first;
        }
    }

    return best;
}

// 建立城市（北/中/南區）
vector<Person> generate_city() {
    vector<Person> people;
    srand(time(0));

    // 北區（正確 A）增加密度
    for (int i = 0; i < 30; i++) {
        double x = 0 + (double)rand() / RAND_MAX * 20;   // 0~20
        double y = 0 + (double)rand() / RAND_MAX * 100;  // 0~100
        people.push_back({x, y, 0});
    }

    // 中區（正確 B，人數減少）
    for (int i = 0; i < 10; i++) {
        double x = 40 + (double)rand() / RAND_MAX * 20;  // 40~60
        double y = 0 + (double)rand() / RAND_MAX * 100;
        people.push_back({x, y, 1});
    }

    // 南區（偏差區：少量 B，多數 C）
    for (int i = 0; i < 30; i++) {
        int label = (i < 5) ? 1 : 2; // 前5人 B, 後25人 C
        double x = 80 + (double)rand() / RAND_MAX * 20;  // 80~100
        double y = 0 + (double)rand() / RAND_MAX * 100;
        people.push_back({x, y, label});
    }

    return people;
}

// 模擬一晚
void simulate_night(vector<Person>& people, Person me, int k, string night_name, bool weighted=false) {
    vector<Neighbor> neighbors;
    int decision = knn_with_neighbors(people, me, k, weighted, neighbors);

    char exits[3] = {'A','B','C'};

    cout << "============================\n";
    cout << night_name << endl;
    cout << "============================\n";

    // 參數
    cout << "參數設定：\n";
    cout << "- K 值: " << k << endl;
    cout << "- 模式: " << (weighted ? "距離加權 KNN" : "一般 KNN") << endl;
    cout << "- 玩家位置: (" << me.x << ", " << me.y << ")" << endl;

    // 鄰居
    cout << "\n選到的鄰居:\n";
    for (int i = 0; i < neighbors.size(); i++) {
        cout << "第 " << i+1 << " 近:\n";
        cout << "  位置: (" << neighbors[i].x << ", " << neighbors[i].y << ")\n";
        cout << "  距離: " << neighbors[i].distance << endl;
        cout << "  選擇出口: " << exits[neighbors[i].label] << endl;
        if (weighted) {
            double w = (neighbors[i].distance == 0) ? 1e9 : 1.0 / (neighbors[i].distance * neighbors[i].distance);
            cout << "  權重: " << w << endl;
        }
        cout << endl;
    }

    // 結果
    cout << "推論結果：\n";
    cout << "預測出口: " << exits[decision] << endl;

    if (decision == 1) {
        cout << "判斷：可能受到偏差區影響\n";
    } else if (decision == 0) {
        cout << "判斷：較安全\n";
    } else {
        cout << "判斷：最終安全出口\n";
    }

    cout << endl;
}

int main() {
    srand(time(0));

    vector<Person> city = generate_city();

    // 玩家位置（中央觀測位置，方便看到三區）
    Person me;
    me.x = 35 + (double)rand() / RAND_MAX * 30;  // x: 35~65
    me.y = 30 + (double)rand() / RAND_MAX * 40;  // y: 30~70
    me.label = -1;

    cout << "玩家隨機生成位置（中央觀測區域）: (" << me.x << ", " << me.y << ")\n";

    // 三夜模擬
    simulate_night(city, me, 1, "第一夜（只看最近）");
    simulate_night(city, me, 3, "第二夜（多數決）");
    simulate_night(city, me, 5, "第三夜（距離平方加權）", true);

    return 0;
}
