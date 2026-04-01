class ListNode {
public:

    int value;
    ListNode* next;

    ListNode(int val): value(val), next(nullptr) {}

    ListNode(int val, ListNode* next): value(val), next(next){}

};

class LinkedList{
private:
    ListNode* head;
    ListNode* tail;

public:

    LinkedList(){
        head = tail = nullptr;
    }

    int get(int index) {
        
        ListNode* temp = head;

        int i = 0;

        while (temp != nullptr){
            if (i == index){
                return temp -> value;
            }
            i++;
            temp = temp -> next;
        }

        return -1;
    }

    void insertHead(int val) {

        ListNode* newNode = new ListNode(val);

        if (head == nullptr){ //does not have to be head.next because head itself is
            //a null ptr;
            // newNode.next = nullptr; not needed because constructor 
            //with just value automatically sets next to nullptr
            head = tail = newNode;
            return;
        }else{
            newNode->next = head;
            //dereference pointer and extract value
            //(*newNode).next = head 
            head = newNode;
        }        
    }
    
    void insertTail(int val) {
        ListNode* newNode = new ListNode(val);

        if (head == nullptr){
            head = tail = newNode;
        } else {
            tail -> next = newNode;
            tail = newNode;
        }

    }

    bool remove(int index) {
        if (head == nullptr) return false; // Empty list

        // Case 1: Remove head (index = 0)
        if (index == 0) {
            ListNode* toDelete = head;
            head = head->next;
            if (head == nullptr) {  // List is now empty
                tail = nullptr;
            }
            delete toDelete;  // Free memory
            return true;
        }

        // Case 2: Remove non-head node (index > 0)
        ListNode* temp = head;
        int i = 0;

        while (temp != nullptr && i < index - 1) {
            temp = temp->next;
            i++;
        }

        // Check if index is out of bounds
        if (temp == nullptr || temp->next == nullptr) {
            return false;
        }

        ListNode* toDelete = temp->next;
        temp->next = temp->next->next;

        // Update tail if we removed the last node
        if (temp->next == nullptr) {
            tail = temp;
        }

        delete toDelete;  // Free memory
        return true;
    }

    vector<int> getValues() {
        ListNode* temp = head;
        vector<int> listValues;

        while (temp != nullptr){
            listValues.push_back(temp->value);
            temp = temp->next;
        }

        return listValues;
    }
};