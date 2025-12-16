#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
    int num,r,temp,sum=0;
    cout<<"Enter number = ";
    cin>>num;

    temp=num;
    while(temp!=0)
    {
        r=temp%10;
        sum=sum+r*r*r;
        temp=temp/10;
    }
    if(sum==num)
    {
        cout<<"The number is Armstrong"<<endl;
    }
    else
        cout<<"The number is not Armstrong"<<endl;


    getch();

}
