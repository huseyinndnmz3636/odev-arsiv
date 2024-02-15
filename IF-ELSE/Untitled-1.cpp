#include <iostream>

using namespace std;

int carpma(int x, int y) {
    int sonuc = 0;
    for (int i = 0; i < y; ++i) {
        sonuc += x;
    }
    return sonuc;
}

int main() {
    int sayi1, sayi2;
    cout << "Iki sayi girin: ";
    cin >> sayi1 >> sayi2;

    cout << "Carpim: " << carpma(sayi1, sayi2) << endl;

    return 0;
}
