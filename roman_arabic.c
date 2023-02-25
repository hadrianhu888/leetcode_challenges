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

char *roman; 
char *arabic;

typedef struct roman_arabic {
    char roman;
    int arabic;
} roman_arabic_t; 

typedef struct arabic_roman {
    int arabic;
    char roman[4];
} arabic_roman_t; 

roman_arabic_t roman_arabic_table[] = {
    {'I', 1},
    {'V', 5},
    {'X', 10},
    {'L', 50},
    {'C', 100},
    {'D', 500},
    {'M', 1000},
    {'\0', 0}
};

arabic_roman_t arabic_roman_table[] = {
    {1, "I"},
    {4, "IV"},
    {5, "V"},
    {9, "IX"},
    {10, "X"},
    {40, "XL"},
    {50, "L"},
    {90, "XC"},
    {100, "C"},
    {400, "CD"},
    {500, "D"},
    {900, "CM"},
    {1000, "M"},
    {0, ""}
};

char *roman_to_arabic(char *roman);
char *arabic_to_roman(char *arabic); 
int main(int argc, char **argv);

char *roman_to_arabic(char *roman)
{
    /**
     * @brief Takes a roman numeral and converts it to an arabic numeral
     * 
     */
    if (roman == NULL) {
        return NULL;
    } else {
        /** 
        * do the conversion 
        */
        int i = 0;
        int j = 0;
        int arabic = 0;
        char *arabic_roman = roman_arabic_table[0].roman;
        arabic = roman_arabic_table[0].arabic;
        while (roman[i]!= '\0') {
            arabic = roman_arabic_table[arabic].arabic;
            arabic_roman[j] = roman_arabic_table[arabic].arabic;
            i++;
            j++;
        }
        return arabic;
    }
}


char *arabic_to_roman(char *arabic)
{
    /**
     * @brief Converts an arabic numeral to roman numeral
     * 
     */
    if (arabic == NULL) {
        return NULL;
    } else {
        /**
         * @brief Do the conversion and keep in mind special cases and the order of the roman numerals
         * 
         */
        int i = 0;
        int j = 0;
        int arabic = 0;
        char *arabic_roman = arabic_roman_table[0].roman;
        roman = arabic_roman_table[0].arabic;
        while (roman[i]!= '\0') {
            arabic = arabic_roman_table[arabic].roman;
            arabic_roman[j] = arabic_roman_table[arabic].arabic;            
            i++;
            j++;
        } 
    }
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

