
//Definition for singly-linked list.
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        ListNode* temp = nullptr;
        
        if (head == nullptr){
            return head;
        } else if (head->next != nullptr){
            temp = head->next;
        } else {
            return head;
        }
        
        head->next = nullptr;

        if (head == nullptr){
            return head;
        }
    
        while (temp != nullptr){
            ListNode* tempNext = temp->next;
            temp->next = head;
            head = temp;
            temp = tempNext; 
        }
        return head;
    }
};
