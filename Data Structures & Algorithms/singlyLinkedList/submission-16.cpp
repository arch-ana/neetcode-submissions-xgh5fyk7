class ListNode{
public:
    int value;
    ListNode* next;

    ListNode(int val):value(val), next(nullptr){}
    ListNode(int val, ListNode* next):value(val), next(next){}

};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;

public:
    LinkedList(): head(nullptr), tail(nullptr){}

    int get(int index) {

        int i = 0;
        ListNode* temp = head;

        if (temp == nullptr){
            return -1;
        }
        else{
            while (temp != nullptr){
                if (i == index){
                    return temp -> value;
                }
                i++;
                temp = temp -> next;
            }
        }

        return -1;
    }

    void insertHead(int val) {

        ListNode* newNode = new ListNode(val);

        //head is currently null
        if (head == nullptr){
            head = tail = newNode;
        }
        //head is not null
        else{
            newNode -> next = head;
            head = newNode;
        }
    }
    
    void insertTail(int val) {

        ListNode* newNode = new ListNode(val);
        
        //head is null
        if (head == nullptr){
            head = tail = newNode;
        }
        //head is not null
        else{
            tail -> next = newNode;
            tail = newNode;
        }
    }

    bool remove(int index) {

        ListNode* temp = head;
        int i = 0;

        //head is null
        if (temp == nullptr){
            return false;
        }

        //only one node
        if (head == tail){
            if (index == 0){
                head = tail = nullptr;
                return true;
            }
            else{
                return false;
            }
        }

        //head being removed in ll with > 1 node
        if (index == 0){
            head = temp->next;
            temp = nullptr;
            return true;
        }

        //finding the node right before the node being removed so that
        //node->next can be deleted 
        while (temp != nullptr && i < index-1){ 
            //less than index minus 1 because at index - 1, it goes
            //one node ahead. so to offset that increase, it is 
            //less than index - 1 and not = index - 1
            temp = temp->next; 
            i++;
        }

        //declaring a nullptr for toDelete
        ListNode* toDelete = nullptr;
        
        //if that node before ToDelete is after tail
        if (temp == nullptr){
            return false;
        }    

        //the node to be deleted is not out of bounds
        if (temp->next != nullptr){
            toDelete = temp->next;
        }else{
            return false;
        }

        // if (toDelete == nullptr) {
        //     return false;
        // }        
        if (toDelete->next == nullptr){
            temp->next = nullptr;
            tail = temp;
            toDelete = nullptr;
            return true;
        }
        else{
            temp->next = temp->next->next;
            toDelete = nullptr;
            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector <int> nodeValues;
        ListNode* temp = head;

        while (temp != nullptr){
            nodeValues.push_back(temp -> value);
            temp = temp -> next;
        }

        return nodeValues;
    }
};
