int main() {
    int number, first = 0, second = 1, next;
    printf("Enter the number:- ");
    scanf("%d", &number);
    printf("Fibonacci series: ");
    for (int i = 1; i <= number; i++) {
        if (i == 1) {
            next = first;
        } else if (i == 2) {
            next = second;
        } else {
            next = first + second;
            first = second;
            second = next;
        } 
        printf("%d ", next);
    }
    printf("\n");
    return 0;
}
