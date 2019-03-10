#include<iostream>
#include <cstring>
#include <string>
#include <fstream>
#include <sstream>
#include <cctype>
#include "windows.h"
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
    flowshop(int pq, int mq)
    {
        machines_quantity=mq;
        parts_quantity =pq;
    }

    void parse(const string &str)
    {
        for(int foo =0; foo<= this->parts_quantity-1; foo++)
        {
            for(int moo=0;moo<=this->machines_quantity-1;moo++)
            {
                char tempone, temptwo;
                tempone = str[10+(4*moo)+(13*foo)];
                temptwo = str[10+(4*moo)+(13*foo)+1];
                if(!iswspace(str[10+(4*moo)+(13*foo)+1]))
                    this->parts_array[foo].partarr[moo]=(int)(tempone-48)*10+temptwo-48;
                else
                    this->parts_array[foo].partarr[moo]=(int)tempone-48;
            }
        }
    }

    void permute(char *a, int l, int r)
    {
        int i;
        if (l == r) {
            cout<<"Obecna permutacja: "<<a<<endl;
            makespan(a);
        }
        else
        {
            for (i = l; i <= r; i++)
            {
                swap((a+l), (a+i));
                permute(a, l+1, r);
                swap((a+l), (a+i));
            }
        }
    }

    void swap(char *x, char *y)
    {
        char temp;
        temp = *x;
        *x = *y;
        *y = temp;
    }

    void makespan(char*a)
    {
        int tspan = 0;
        string tempstr(a);
        part temparr[20];
        int cond = tempstr.length();
        for(int foo=0; foo<=cond-1; foo++)
        {
            temparr[foo] = this->parts_array[(tempstr[foo])-49];
        }
        int tMachExec[20];
        int isFirstTime = 1;
        for( int moo=0; moo<1; moo++)
        {
            for (int foo = 0; foo <= this->parts_quantity-1; foo++)
            {
                if(isFirstTime) {
                    tMachExec[foo] = temparr[foo].partarr[0];
                    isFirstTime =0;
                }
                else {
                    tMachExec[foo] = temparr[foo].partarr[0] + tMachExec[foo - 1];
                }
            }
        }
        isFirstTime=1;
        for(int moo=1; moo <= machines_quantity-1; moo++)
        {
            for(int foo=0; foo<=this->parts_quantity-1; foo++)
            {
                if(isFirstTime) {
                    tMachExec[foo] = temparr[foo].partarr[moo] + tMachExec[foo];
                    isFirstTime=0;
                }
                else
                {
                    tMachExec[foo] = temparr[foo].partarr[moo] + max(tMachExec[foo-1], tMachExec[foo]);
                }
            }
        }
        cout<<"Czas wykonania calkowitego: "<< tMachExec[this->parts_quantity-1]<<endl;
    }
};

int main() {
    int pq;
    int mq;
    int choice=1;
    while(choice)
    {
        cout<<"Wybierz cyfre od 1 do 6 by wczytac instancje"<<endl;
        ifstream inFile;
        cin>>choice;
        switch(choice) {
            case 1:
                inFile.open("tabelka1.txt");
                break;
            case 2:
                inFile.open("tabelka2.txt");
                break;
            case 3:
                inFile.open("tabelka3.txt");
                break;
            case 4:
                inFile.open("tabelka4.txt");
                break;
            case 5:
                inFile.open("tabelka5.txt");
                break;
            case 6:
                inFile.open("tabelka6.txt");
                break;
            case 0:
                return 0;
        }
        stringstream strStream;
        strStream << inFile.rdbuf();
        string str = strStream.str();
        cout << "Wczytany plik:" << endl << str << endl;
        pq = (int) str[2] - 48;
        mq = (int) str[6] - 48;
        flowshop scena(pq, mq);
        scena.parse(str);
        char tempstr[99] = "0";
        for (int foo = 0; foo <= scena.parts_quantity - 1; foo++) {
            tempstr[foo] = foo + 49;
        }
        int n = strlen(tempstr);
        scena.permute(tempstr, 0, n - 1);
    }
}
