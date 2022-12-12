#include <iostream>
#include <vector>

void addToBuffer(std::vector<uint16_t> &buffer, int index, int value_to_add){
    uint16_t current = buffer[index];
    if (current + value_to_add > 255) buffer[index] = current % 256 - 256;
    if (current + value_to_add < 0) buffer[index] = current % 256 + 256;
    buffer[index]+= value_to_add;
    return;
}

void openBracketCase(std::vector<uint16_t> &buffer, const std::string &code, int data_pointer, int instruction_pointer){
    if (buffer[data_pointer] == 0){
        int level = 1;
        while(level > 0){
            instruction_pointer++;
            switch(code[instruction_pointer]){
            case '[':
                level++;
                break;
            case ']':
                level--;
                break;
            default:
                break;
            }
        }
      instruction_pointer++;
    }
    return;
}

void closedBracketCase(std::vector<uint16_t> &buffer, const std::string &code, int data_pointer, int &instruction_pointer){
    if (buffer[data_pointer] != 0){
        int level = -1;
        while(level < 0){
            instruction_pointer--;
            switch(code[instruction_pointer]){
            case '[':
                level++;
                break;
            case ']':
                level--;
                break;
            default:
                break;
            }
        }
      instruction_pointer--;
    }
    return;
}

std::string brainLuck(const std::string &code, const std::string &input) {
    std::vector<uint16_t> buffer (3000,0);
    int data_pointer = 0;
    std::string output = "";
    auto it = input.begin();

    // std::cout<<code<<"\n\n";
    // std::string block_spaces = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    // std::cout<<input<<block_spaces<<block_spaces<<block_spaces<<block_spaces;
    for (int instruction_pointer = 0; instruction_pointer < code.length(); instruction_pointer++){
    //   std::cout<<code[instruction_pointer];
      switch (code[instruction_pointer])
        {
        case '>':
            data_pointer++;
            break;

        case '<':
            data_pointer--;
            break;
        
        case '+':
            addToBuffer(buffer,data_pointer,1);
            break;

        case '-':
            addToBuffer(buffer,data_pointer,-1);
            break;

        case '.':
            output.append(1,(char) buffer[data_pointer]);
            std::cout<<"\noutput mutated: \n"<<output<<"\n";
            break;

        case ',':
            buffer[data_pointer] = 0;
            addToBuffer(buffer,data_pointer, *it);
            it++;
            break;

        case '[':
            openBracketCase(buffer, code, data_pointer, instruction_pointer);
            break;
        
        case ']':
            closedBracketCase(buffer, code, data_pointer, instruction_pointer);
            break;

        default:
            break;
        }
    }
    std::cout << "\n" << output << "\n\n\n";
    return output;
}


int main(){
    // std::string tw = "codewars";
    // tw.append(1,255);
    // std::cout << brainLuck(",+[-.,+]", tw ) << "\n";

    // std::string mw = "codewars";
    // mw.append(1,(char)0);
    // std::cout<<brainLuck(",[.[-],]",mw)<<"\n";


    // std::string dw;
    // dw.append(1, (char) 7);
    // dw.append(1, (char) 3);
    // std::cout<<brainLuck(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.",dw)<<"\n";

    std::string code = ",>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]";
    std::string input = "";
    input.append(1,(char) 10);
    std::cout << brainLuck(code,input) << "\n";
    return 0;
}