/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* sortedListHead;
        ListNode* sortedListIter;
        ListNode* iter1 = list1;
        ListNode* iter2 = list2;

        if (iter1 == nullptr && iter2 == nullptr){
            return nullptr;
        } else if (iter1 == nullptr){
            return iter2;
        } else if (iter2 == nullptr){
            return iter1;
        } else {
            if (iter1->val < iter2->val){
                sortedListHead = iter1;
                iter1 = iter1->next;
            } else {
                sortedListHead = iter2;
                iter2 = iter2->next;
            }
            sortedListIter = sortedListHead;

            while (iter1 != nullptr && iter2 != nullptr){
                if (iter1->val < iter2->val){
                    sortedListIter->next = iter1;
                    iter1 = iter1->next;
                } else {
                    sortedListIter->next = iter2;
                    iter2 = iter2->next;
                }
                sortedListIter = sortedListIter->next;
            }

            if (iter1 == nullptr && iter2 == nullptr){
                return sortedListHead;
            } else if (iter1 == nullptr){
                sortedListIter->next = iter2;
            } else {
                sortedListIter->next = iter1;
            }

            return sortedListHead;           
        }

        
    }
};
