#include <iostream>
#include <vector>
#include <deque>
#include <ctime>
using namespace std;

// =========================
// Stack
// =========================
class Stack {
private:
    vector<int> items;
    int capacity;

public:
    Stack(int cap = 3) { capacity = cap; }

    void push(int item) {
        if ((int)items.size() >= capacity) {
            cout << "[Stack] Overflow!" << endl;
            return;
        }
        cout << "[Stack] Push " << item << endl;
        items.push_back(item);
    }

    void pop() {
        if (items.empty()) {
            cout << "[Stack] Underflow!" << endl;
            return;
        }
        cout << "[Stack] Pop " << items.back() << endl;
        items.pop_back();
    }

    void peek() {
        if (!items.empty())
            cout << "[Stack] Top: " << items.back() << endl;
        else
            cout << "[Stack] Empty!" << endl;
    }

    void print() {
        cout << "  Stack: ";
        for (size_t i = 0; i < items.size(); i++) cout << items[i] << " ";
        cout << endl;
    }
};

// =========================
// Queue
// =========================
class Queue {
private:
    deque<int> items;
    int capacity;

public:
    Queue(int cap = 3) { capacity = cap; }

    void enqueue(int item) {
        if ((int)items.size() >= capacity) {
            cout << "[Queue] Overflow!" << endl;
            return;
        }
        cout << "[Queue] Enqueue " << item << endl;
        items.push_back(item);
    }

    void dequeue() {
        if (items.empty()) {
            cout << "[Queue] Underflow!" << endl;
            return;
        }
        cout << "[Queue] Dequeue " << items.front() << endl;
        items.pop_front();
    }

    void print() {
        cout << "  Queue: ";
        for (size_t i = 0; i < items.size(); i++) cout << items[i] << " ";
        cout << endl;
    }
};

// =========================
// 主程式
// =========================
int main() {
    Stack s(3);
    Queue q(3);

    int a, b, c;
    clock_t program_start = clock();

    // ===== Stack 操作 =====
    cout << "Enter 3 values for Stack: ";
    cin >> a >> b >> c;

    clock_t stack_start = clock();

    // push 3 次
    s.push(a);
    s.push(b);
    s.push(c);

    // pop 3 次
    for (int i = 0; i < 3; i++) s.pop();

    // peek 顯示最後狀態
    s.peek();

    clock_t stack_end = clock();
    double stack_time = double(stack_end - stack_start) / CLOCKS_PER_SEC;
    cout << "\n[Stack Execution Time]: " << stack_time << " seconds\n";

    // ===== Queue 操作 =====
    cout << "\nEnter 3 values for Queue: ";
    cin >> a >> b >> c;

    clock_t queue_start = clock();

    // enqueue 3 次
    q.enqueue(a);
    q.enqueue(b);
    q.enqueue(c);

    // dequeue 3 次
    for (int i = 0; i < 3; i++) q.dequeue();

    clock_t queue_end = clock();
    double queue_time = double(queue_end - queue_start) / CLOCKS_PER_SEC;
    cout << "\n[Queue Execution Time]: " << queue_time << " seconds\n";

    clock_t program_end = clock();
    double total_time = double(program_end - program_start) / CLOCKS_PER_SEC;

    cout << "\n===== Total Program Execution Time =====" << endl;
    cout << "Total time: " << total_time << " seconds" << endl;

    cout << "\n===== Time Complexity =====" << endl;
    cout << "Stack: push/pop/peek = O(1), print = O(n)" << endl;
    cout << "Queue: enqueue/dequeue = O(1), print = O(n)" << endl;

    return 0;
}
	
