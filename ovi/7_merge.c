#include<stdio.h>
#include<stdlib.h>
void bubble_sort(int *arr,int size)
{
    FILE *file3;
    file3= fopen("7_output.txt","a");

    for(int i=0;i<size-1;i++)
    {
        for(int j=0;j<size-i-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    for(int m=0;m<size;m++)
    {
        fprintf(file3,"%d\n",arr[m]);
        printf("%d\n",arr[m]);
    }
}
int marge(int *arr1,int *arr2,int i,int j,int arrlen)
{
    int p=0,m=0;
    while(p<=j-1)
    {
        arr1[i]=arr2[p];
        p++;
        i++;
    }
    bubble_sort(arr1,arrlen);
}
int main()
{
    FILE *file1,*file2;
    int arr1[50],arr2[100],i=0,j=0;
    file1= fopen("7_Input1.txt","r");
    file2= fopen("7_Input2.txt","r");

    if(file1==NULL)
    {
        printf("Input File1 Not Found");
        exit(0);
    }
      if(file2==NULL)
    {
        printf("Input File2 Not Found");
        exit(0);
    }
        while(fscanf(file1,"%d",&arr1[i])==1)
    {
        i++;
    }
    while(fscanf(file2,"%d",&arr2[j])==1)
    {
        j++;
    }
    int arrlen=i+j;
    marge(arr1,arr2,i,j,arrlen);
    fclose(file1);
    fclose(file2);
    return 0;
}
