#include <string>
#include <iostream>
#include <algorithm>


// TODO need to actually parse array to confirm there are no parenthesis
void stack_dump(std::string &result, std::string &op_stack){
    if (op_stack.find('(') != std::string::npos) {
        std::size_t found = op_stack.find_last_of('(');
        std::string inner = op_stack.substr(found+1);
        std::reverse(inner.begin(), inner.end());
        result += inner;
        op_stack.erase(found+1);
    } else {
        std::reverse(op_stack.begin(), op_stack.end());
        result += op_stack;
        op_stack = "";
    }
}

std::string to_postfix(std::string infix) {
    std::string result = "";
    std::string op_stack = "";
    for (char chr : infix){
        switch (chr){
            case '(': op_stack += chr; break;
            case ')': 
                while (true){
                    if(op_stack.back() == '(') break;
                    result+=op_stack.back();
                    op_stack.erase(op_stack.end()-1);
                }
                op_stack.erase(op_stack.end()-1);
                break;
            case '^': op_stack += chr; break;
            case '*': 
                if (op_stack.back() == '+' & op_stack.back() == '-') stack_dump(result, op_stack);
                op_stack += chr; break;
            case '/': 
                if (op_stack.back() != '+' & op_stack.back() != '-') stack_dump(result, op_stack);
                op_stack += chr; break;
            case '+': 
                if (!op_stack.empty() & op_stack.back() != '(') stack_dump(result, op_stack);
                op_stack += chr; break;
            case '-':
                if (!op_stack.empty() & op_stack.back() != '(') stack_dump(result, op_stack);
                op_stack += chr; break;
            default: result += chr;
        }
    }
    if (!op_stack.empty()) stack_dump(result, op_stack);
    return result;
}

class Assert{
    public:
        template <typename T>
        static void That(T first, T second){
            if (first == second) std::cout<<"check passed\n";
            else std::cout <<"check failed: " << first << " " << second << '\n';
        }
};

template <typename T>
T Equals(T value){
    return value;
}
int main(){
    // Assert::That<std::string>(to_postfix("2+7*5"), Equals<std::string>("275*+"));
    // Assert::That<std::string>(to_postfix("3*3/(7+1)"), Equals<std::string>("33*71+/"));
    // Assert::That<std::string>(to_postfix("5+(6-2)*9+3^(7-1)"), Equals<std::string>("562-9*+371-^+"));
    Assert::That<std::string>(to_postfix("(5-4-1)+9/5/2-7/1/7"), Equals<std::string>("54-1-95/2/+71/7/-"));
    return 0;
}