// samsung.cpp

#include <vector>
#include <iostream>

void halve_values(std::vector<double>& numbers)
    {
        for (int i = 0; i < numbers.size(); i++){
            numbers[i]/=2;
        }
    }
void quad(std::vector<double> numbers) {
    for(int i =0; i<numbers.size(); i++){
        numbers[i] *=4;
    }
}

int main(void) {
    std::vector<double> numbers = {0.0, 0.5, 1.0, 1.5, 2.0};
    quad(numbers);
    halve_values(numbers);
    double sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += numbers[i];
    }
    std::cout<<sum<<std::endl;
}