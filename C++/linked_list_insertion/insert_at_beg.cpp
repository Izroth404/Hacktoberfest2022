#include <iostream>
using namespace std;
int count = 0;

struct node
{
    int data;
    node *next;
    node()
    {
        data = 0;
        next = NULL;
    }
    node(int x)
    {
        data = x;
        next = NULL;
    }
};
void createList(node *head, int n)
{
    node *newNode, *temp;
    int data, i;
    cout << "Enter the Data of Node 1: ";
    cin >> data;
    if (head == NULL)
    {
        printf("Unable to allocate memory.");
        exit(0);
    }
    head->data = data;
    head->next = NULL;
    temp = head;
    for (i = 2; i <= n; i++)
    {
        cout << "Enter the data of node " << i << ": ";
        cin >> data;
        newNode = new node(data);
        if (newNode == NULL)
        {
            printf("Unable to allocate memory. ");
            break;
        }
        temp->next = newNode;
        temp = temp->next;
    }
}
int traverseList(node *head)
{
    node *temp;
    count = 0;
    if (head == NULL)
    {
        printf("List is Empty. ");
        return count;
    }
    temp = head;
    while (temp != NULL)
    {
        cout << "Data = " << temp->data << endl;
        temp = temp->next;
        count++;
    }
    cout << "The total number of Elements in LinkedList are " << count;
    return count;
}
node *insertatbeg(node *head, int data)
{
    node *newNode = new node(data);
    if (newNode == NULL)
    {
        printf("Unable to allocate memory.");
    }
    newNode->next = head;
    return newNode;
}
int main()
{
    int i = 0, n = 0;
    cout << "Please enter the number of nodes : ";
    cin >> n;
    cout << "Enter the values: " << endl;
    node *head = new node();
    createList(head, n);
    cout << "\nData in the list \n"<< endl;
    count = (traverseList(head));
    cout << endl<< "Enter the element you want to insert in the beginning of the linked list :";
    cin >> n;
    head = insertatbeg(head, n);
    count = traverseList(head);
}
