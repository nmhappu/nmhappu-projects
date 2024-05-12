#include <iostream>
#include <string>
#include <unordered_map>
#include <functional>

/* wsl */

int x; 
int y;

void add()  {int sum = x + y;
            std::cout << sum << "\n";}
void sub()  {int sub = x - y;
            std::cout << sub << "\n";}
void mult() {int mult = x * y;
            std::cout << mult << "\n";}
void by()   {int by = x / y;
            std::cout << by << "\n";}

int main() {

    std::unordered_map<std::string, std::function<void()>> functions = { 
        {"add", add}, 
        {"sub", sub},
        {"mult", mult},
        {"by", by}};
    
    std::string s;
    
    std::cout << "Functions: \n add, sub, mult, by \n => ? ";
    std::cin >> s;
    
    std::cout << "X => ";
        std::cin >> x;

    std::cout << "Y => ";
        std::cin >> y;

    functions[s]();
    return 0 ;
}
