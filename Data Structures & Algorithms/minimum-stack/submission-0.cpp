class MinStack {
public:

    stack<pair<int, int>> newStack;

    MinStack() {
    }
    
    void push(int val) {
        if (newStack.empty() || val < newStack.top().second){
            newStack.push({val,val});
        }else{
            newStack.push({val,newStack.top().second});
        }
    }
    
    void pop() {
        newStack.pop();
    }
    
    int top() {
        return newStack.top().first;
    }
    
    int getMin() {
        return newStack.top().second;
    }
};
