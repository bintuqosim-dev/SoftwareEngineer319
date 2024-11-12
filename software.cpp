#include <iostream>
#include <cstdint>
//big endian code prepare by boburjon
bool is_little_endian() {
    uint16_t x = 0x1;
    return *((uint8_t*)&x) == 0x1;
}

int main() {
    if (is_little_endian()) {
        std::cout << "System is Little Endian" << std::endl;
    } else {
        std::cout << "System is Big Endian" << std::endl;
    }
    return 0;
}
