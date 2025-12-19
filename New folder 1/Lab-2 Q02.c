#include<stdio.h>
int main()
{
    int x;
    printf("Input an Integer: ");
    scanf("%d",&x);

    if(x%3==0 && x%5==0)
        printf("FIZZBUZZ");
    else if(x%3==0)
        printf("FIZZ");
   else if(x%5==0)
        printf("BUZZ");
    else
        printf("Invalid");


    getch();
}
