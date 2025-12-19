#include<stdio.h>
struct student
{
    char name[80];
    int marks;
    char grade;
};
char checking_grade(int marks)
{
  if(marks>=80 && marks<=100){
    return 'A';
  }
  else if(marks>=70 && marks<=79){
    return 'B';
  }
  else if(marks>=60 && marks<=69){
    return 'C';
  }
  else if(marks>=50 && marks<=59){
    return 'D';
  }
  else if(marks>40 && marks<=49){
    return 'E';
  }
  else {
    return 'F';
  }

}
int main()
{
    FILE *file1, *file2;
    struct student stdinfo;
    file1=fopen("3_lab_input.txt","r");
    file2=fopen("3_lab_out.txt","a");
    while(!feof(file1))
    {
        fscanf(file1, "%s", &stdinfo.name);
        fscanf(file1, "%d",&stdinfo.marks);

        printf("%s ",stdinfo.name);
        printf("%d ",stdinfo.marks);
        printf("%c ",checking_grade(stdinfo.marks));
        printf("\n");

        fprintf(file2,"%s ",stdinfo.name);
        fprintf(file2, "%d ",stdinfo.marks);
        fprintf(file2,"%c ",checking_grade(stdinfo.marks));
        fprintf(file2,"\n");
    }
    fclose(file1);
    fclose(file2);
    return 0;


}
