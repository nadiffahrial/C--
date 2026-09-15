#include <iostream>

using namespace std;

int main() {
    // DEKLARASI
    int nilai;
    char grade;

    // DESKRIPSI
    cout << "Masukkan nilai: ";
    cin >> nilai;

    if (nilai >= 85 && nilai <= 100) {
        grade = 'A';
    } 
    else if (nilai >= 70 && nilai <= 84) {
        grade = 'B';
    } 
    else if (nilai >= 60 && nilai <= 69) {
        grade = 'C';
    } 
    else {
        grade = 'E';
    }

    cout << "Grade: " << grade << endl;

    return 0;
}