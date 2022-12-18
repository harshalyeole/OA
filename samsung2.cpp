// samsung.cpp

int* arr = new int[10];
for (int i = 0 ; i < 10; i++) {
    arr[i] = i * 100;
}
int t1 = arr[4];
int t2 = *(arr + 4);
int t3 = (int)(&arr + 4);
int t4 = *arr + 4;

std::cout<<t1::endl;
std::cout<<t2::endl;
std::cout<<t3::endl;
std::cout<<t4::endl;