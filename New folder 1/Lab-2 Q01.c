#include<stdio.h>
int main()
{
    int y;
    printf("Input Year: ");
    scanf("%d",&y);

    if(y%100==0)
    {
        if(y%400==0)
            printf("Given Year is Leap Year");
        else
            printf("Given year is not Leap year");
    }
    else
    {
        if(y%4==0)
            printf("Given Year is Leap Year");
        else
            printf("Given Year is not Leap Year");
    }
}
