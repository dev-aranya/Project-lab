#include<stdio.h>
int main()
{
    int a,b,c;
    printf("Input three integer value: ");
    scanf("%d %d %d",&a,&b,&c);
    int x=a*a, y=b*b, z=c*c;
    if(x+y==z || y+z==x || x+z==y)
        printf("Right angle triangle");
    else
        printf("It is not right angle triangle");

    getch();

}
