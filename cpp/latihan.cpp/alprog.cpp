#include<iostream>
using namespace std;
int main(){
    int i;
    cout<<"masukan nilai:";
    cin>>i;
    if (i>=85){
        cout<<"NILAI ANDA PUAS";
    }
    else if (i<85){
        cout<<"NILAI ANDA KURANG";
    }
    return 0;
}