#include <stdio.h>
int main() {
  char name[50];
  printf("Enter your name: ");
  gets(name);
  puts(name);
  return 0;
}