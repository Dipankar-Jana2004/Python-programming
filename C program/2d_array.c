#include<stdio.h>
int main(){
    int i,j,row1,col1,arr[30][30];
    printf("Enter the no of rows and column of 2 dimensional array:-");
    scanf("%d",&row1,&col1);
    for ( i=0;i<row1; i++){
        for ( j= 0; j<col1; j++) {
            printf("enter array elements:-");
            scanf("%d",arr[i][j]);

        }
    printf("\nArray elenments are:-");
    for ( i = 0; i<row1; i++) {
        for ( j = 0; i <col1; j++){
            printf("enter array elements:-");
            scanf("%d",arr[i][j]);

        }
        
    }
    printf("\narray elements are:-");
    for ( i = 0; i <row1; i++){
        for ( j = 0; i<col1; i++){
            printf("\narr[%d][%d]=%d,i,j,arr[i][j]");
        }
    }
    }
    return 0;
    
}