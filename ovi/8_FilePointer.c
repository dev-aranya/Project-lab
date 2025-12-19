#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    int n;

    fp = fopen("8_input.txt", "r");
    if (fp == NULL)
    {
        printf("fp file not exist\n");
        exit(0);
    }

    printf("Enter value of n= ");
    scanf("%d", &n);

    fseek(fp, -n, 2);
    char arr1[n + 1];

    for (int i = 0; i < n; i++)
    {
        fscanf(fp, "%c", &arr1[i]);
    }

    //arr1[n]= '\0';
    printf("Last n characters: %s\n",arr1);
    rewind(fp);

    char arr2[n + 1];

    for (int i = 0; i < n; i++)
    {
        fscanf(fp, "%c", &arr2[i]);
    }

    //arr2[n] = '\0';
    printf("First characters: %s\n",arr2);

    fclose(fp);

    return 0;
}
