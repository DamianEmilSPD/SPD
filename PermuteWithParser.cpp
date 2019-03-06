#include<iostream>
#include <cstring>
#include <string>
#include <fstream>
#include <sstream>
#include <cctype>
//#include <algorithm>
//include <vector>
//#include <cstdlib>
using namespace std;


class part
{
public:
    int partarr[3];
};

class flowshop
{
public:
    int machines_quantity;
    int parts_quantity;
    part parts_array[20];
    flowshop(const int &pq, const int &mq)
    {
        machines_quantity=mq;
        parts_quantity =pq;
    }
};

void swap(char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void permute(char *a, int l, int r)
{
    int i;
    if (l == r)
        printf("%s\n", a);
    else
    {
        for (i = l; i <= r; i++)
        {
            swap((a+l), (a+i));
            permute(a, l+1, r);
            swap((a+l), (a+i)); //backtrack
        }
    }
}

int main() {
    /*char str[] = "123";

    int n = strlen(str);
    permute(str, 0, n-1);*/
    /*ifstream inFile;
    inFile.open("tabelka1.txt");

    stringstream strStream;
    strStream << inFile.rdbuf();
    string str = strStream.str();

    cout << str << endl;*/
    int pq;
    int mq;

    ifstream inFile;
    inFile.open("tabelka1.txt");
    stringstream strStream;
    strStream << inFile.rdbuf();
    string str = strStream.str();
    cout <<"Wczytany plik:"<<endl<< str << endl;

    pq = (int)str[2] -48;
    mq = (int)str[6] -48;
    flowshop scena(pq, mq);
    for(int foo =0; foo<= mq-1; foo++)
    {
        for(int moo=0;moo<=pq-1;moo++)
        {
            char tempone, temptwo;
            tempone = str[10+(4*moo)+(13*foo)];
            temptwo = str[10+(4*moo)+(13*foo)+1];
            if(!iswspace(str[10+(4*moo)+(13*foo)+1]))
                scena.parts_array[foo].partarr[moo]=(int)(tempone-48)*10+temptwo-48;
            else
                scena.parts_array[foo].partarr[moo]=(int)tempone-48;
        }
    }
    cout<<"Czesc pierwsza czasy"<<endl;
    cout<<scena.parts_array[0].partarr[0]<<endl;
    cout<<scena.parts_array[0].partarr[1]<<endl;
    cout<<scena.parts_array[0].partarr[2]<<endl;
    cout<<"Czesc druga czasy"<<endl;
    cout<<scena.parts_array[1].partarr[0]<<endl;
    cout<<scena.parts_array[1].partarr[1]<<endl;
    cout<<scena.parts_array[1].partarr[2]<<endl;
    cout<<"Czesc trzecia czasy"<<endl;
    cout<<scena.parts_array[2].partarr[0]<<endl;
    cout<<scena.parts_array[2].partarr[1]<<endl;
    cout<<scena.parts_array[2].partarr[2]<<endl;
    //cout<<scena.machines_quantity<<endl;
    //cout<<scena.parts_quantity<<endl;
}

