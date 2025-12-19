#include<stdio.h>
int main()
{
    int marks;
    printf("Input marks: ");
    scanf("%d",&marks);

    switch(marks/10)
    {
        case 8 ... 10:  //Range
        printf("A+");
        break;

        case 7:
        printf("A");
        break;

        case 6:
        printf("B+");
        break;

        case 5:
        printf("B");
        break;

        case 4:
        printf("C");
        break;

        case 1 ... 3:
        printf("F");
        break;

        default:
        printf("Invalid Input");
        break;
    }



}

