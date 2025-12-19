#include<stdio.h>
int main()
{
    int a,b,c;
    printf("Input three numbers: ");
    scanf("%d %d %d",&a,&b,&c);

    if(a<b)
    {
        if(a<c)
            printf("%d is the smallest number ",a);
        else
            printf("%d is the smallest number ",c);
    }
    else
    {
        if(c<b)
            printf("%d id the smallest number",c);
        else
            printf("%d is the smallest number ",b);
    }
}
