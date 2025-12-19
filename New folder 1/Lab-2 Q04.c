#include<stdio.h>
int main()
{
    int marks;
    printf("Input marks: ");
    scanf("%d",&marks);

    if(marks<=100 && marks>=80)
        printf("A+");
    else if(marks<=79 && marks>=70)
        printf("A");
    else if(marks<=69 && marks>=60)
        printf("B+");
    else if(marks<=59 && marks>=50)
        printf("B");
    else if(marks<=49 && marks>=40)
        printf("C");
    else if(marks<=39)
        printf("F");
    else
        printf("You put wrong marks");

    getch();
}

