#include <iostream>
using namespace std;

class Node{
    int data;
    Node* next;
    public:
    Node();
    Node(int a)
    {data = a;}
    
};

class LL{
    Node* head;
    public:
    void insert(int data);
    void display();
};


int main()
{
    LL obj;
    return 0;
}