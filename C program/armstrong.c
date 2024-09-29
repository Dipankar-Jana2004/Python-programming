#include <stdio.h>
#include <math.h>
void armstrom(int a){
    int rev, arm, sum = 0, temp = a;
    while (a > 0) {
        rev= a % 10;
        sum +=(rev*rev*rev);
        a = a / 10;
    }
    if (temp == sum){
        printf("armstrom number ");
    }
    else{
        printf("not armstrom number");
    }
}
int main(){
    int x;
    printf("enter the number:- ");
    scanf("%d", &x);
    armstrom(x);
}