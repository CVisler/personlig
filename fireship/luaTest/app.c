#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
    char c = get_char("Char: ");
    int i = tolower(c);
    printf("%c\n", i);
}