/**
 * @file roman_arabic.c
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2023-02-24
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h> 
#include <errno.h>
#include <limits.h>

char *roman; 
char *arabic;

typedef struct roman_arabic {
    char *roman; 
    char *arabic; 
} roman_arabic_t; 

typedef struct arabic_roman {
    char *arabic;
    char *roman;
} arabic_roman_t;

roman_arabic_t roman_arabic_table[] =
{   {"I", "1"},    {"II", "2"},    {"III", "3"},    {"IV", "4"},
    {"V", "5"},    {"VI", "6"},    {"VII", "7"},    {"VIII", "8"},
    {"IX", "9"},   {"X", "10"},    {"XL", "40"},    {"L", "50"},
    {"XC", "90"},  {"C", "100"},   {"CD", "400"},   {"D", "500"},
    {"DC", "600"}, {"DCC", "700"}, {"DCCC", "800"}, {"CM", "900"},
    {"M", "1000"}, {"", ""}}; 

arabic_roman_t arabic_roman_table[] = 
{   {"1", "I"},    {"2", "II"},    {"3", "III"},    {"4", "IV"},
    {"5", "V"},    {"6", "VI"},    {"7", "VII"},    {"8", "VIII"},
    {"9", "IX"},   {"10", "X"},    {"40", "XL"},    {"50", "L"},
    {"90", "XC"},  {"100", "C"},   {"400", "CD"},   {"500", "D"},
    {"600", "DC"}, {"700", "DCC"}, {"800", "DCCC"}, {"900", "CM"},
    {"1000", "M"}, {"", ""}};

char *roman_to_arabic(char *roman);
char *arabic_to_roman(char *arabic); 
int main(int argc, char **argv);

char *roman_to_arabic(char *roman)
{
    int i;
    char *arabic;
    arabic = (char *)malloc(sizeof(char) * (strlen(roman) + 1));
    for (i = 0; roman[i]!= '\0'; i++)
    {
        arabic[i] = (char)roman_arabic_table[roman[i]].arabic;
    }
    arabic[i] = '\0';
    return arabic;
}

char *arabic_to_roman(char *arabic)
{
    int i;
    char *roman;
    roman = (char *)malloc(sizeof(char) * (strlen(arabic) + 1));
    for (i = 0; arabic[i]!= '\0'; i++)
    {
        roman[i] = (char)arabic_roman_table[arabic[i]].roman;
    }
    roman = (char *)malloc(sizeof(char) * (strlen(arabic) + 1));
    return roman;
}


int main(int argc, char **argv)
{
    /**
     * @brief Main function
     * 
     */
    if (argc != 3) {
        printf("Usage: %s roman|arabic roman|arabic\n", argv[0]);
        return 1;
    } else {
        if (strcmp(argv[1], "roman") == 0) {
            roman = argv[2];
            arabic = roman_to_arabic(roman);
            printf("%s = %s\n", roman, arabic);
        } else if (strcmp(argv[1], "arabic") == 0) {
            arabic = argv[2];
            roman = arabic_to_roman(arabic);
            printf("%s = %s\n", arabic, roman);
        } else {
            printf("Usage: %s roman|arabic roman|arabic\n", argv[0]);
            return 1;
        }
    }
    return 0;
}

