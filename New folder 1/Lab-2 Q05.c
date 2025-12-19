#include<stdio.h>
int main()
{
    int a,b;
    char op;
    printf("Input One of These operator(+,-,*,/,%%): ");
    scanf("%c",&op);
    printf("Input two Integer Value: ");
    scanf("%d %d",&a,&b);
    switch(op)
    {
    case'+':
        printf("%d+%d=%d",a,b,a+b);
        break;
    case'-':
        printf("%d-%d=%d",a,b,a-b);
        break;
    case'*':
        printf("%d*%d=%d",a,b,a*b);
        break;
    case'/':
        printf("%f/%f=%f",(float)a,(float)b,(float)a/b);
        break;
    case'%':
        printf("%d%%d=%d",a,a%b);
        break;
    default:
        printf("Invalid Input");
        break;

        getch();





    }


}
