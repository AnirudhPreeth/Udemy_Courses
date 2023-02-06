/*
Section 7: Comments and Format Specification. 
*/

/*
Two ways to make comments - // or even /* */ // is a single line comment. /* and */ is a multi line comment. */ 

#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("I am %d years old\n", 20);
    return 0;
}

// %d acts as placeholder which will be replaced by the number that comes right after the first comma. 

#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("I am %d years old\n", 21);
    return 0;
}

//Now it prints 21. 

/*
printf("Today I am %d and next year I'm going to be %d years old\n", 20, 21);
printf("My average grade : %d\n", 93.7);
In first printf, we get 20 and 21. 
In second printf, we get a strange number that is not 93.7. 
For floating point numbers - %f is correct. 

printf("My average grade : %1f\n", 93.7);
Also, you can limit the total amount of zeros after the floating point just by specifying ...
...how many digits you would like to see on the screen after this floating point itself.
You specify .1 before the F, and this means that there will be only one digit after the floating point.
*/

/*
%d or %i - A decimal integer or signed integer 

%c - Signed character 

%f - Signed float

%e - A floating-point number

%s - A string or sequence of character 

%lf - double

%Lf - Long double 

%o - Octal integer

%u - Short unsigned integer

%ld - Long decimal integer

%x - Hexadecimal integer

%p - Print memory address in the hexadecimal form
*/

/*
Exercises. 

Given 10 exercises to practice format specifiers using the "printf" function.
Write down what will be printed at each of them and then make sure of that by 
testing the results in Code::Blocks.

1. printf("We have %d coins in the bank\n", 100);
2. printf("We have %f coins in the bank\n", 125.7);
3. printf("Year = %d\n", 2020);
4. printf("Your average grade is: %f \n", 95.13);
5. printf("num1 = %d, num2 = %d, sum = %d \n", 5, 7, 5+7);
6. printf("num1 = %f, num2 = %f, sum = %f \n", 5.2, 7.3, 9.5);
7. printf("num1 = %d, num2 = %d, sub = %d \n", 5, 3, 5-3);
8. printf("a = %d, b = %d, sum = a + b = %d \n", 3, 5, 3+5);
9. printf("a = %d, b = %d, sum = %d + %d = %d \n", 3, 5, 3, 5, 3+5);
10. printf("a = %d, b = %d, sum = a + b = %d + %d = %d \n", 3, 5, 3, 5, 3+5);

In the above printf statements -
1. 10 will be printed. 
2. 125.7 will be printed.
3. 2020 will be printed.
4. 95.13 will be printed.
5. 5, 7, 12 will be printed. (5+7 = 12, so the compiler will calculate that).
6. 5.2, 7.3, 9.5 will be printed. 
7. 5, 3, 2 will be printed.
8. 3, 5, 8 will be printed.
9. 3, 5, 3 + 5, 8 will be printed. 
10. 3, 5, 3+5, 8 will be printed. 

The above are my solutions to the given exercise. 
*/

//Milestone #1 - Building Your First Calculator A. 

#include <stdio.h>
int main()
{
    printf("The sum of the two numbers are : num1 = %d, num2 = %d, sum = %d\n", 2, 3, 2+3);
    printf("The subtraction of the two numbers are : num1 = %d, num2 = %d, subtraction = %d\n", 3, 2, 3-2);
    printf("The multiplication of the two numbers are : num1 = %d, num2 = %d, multiplication = %d\n", 3, 2, 3*2);
    printf("The division of the two numbers are : num1 = %f, num2 = %f, division = %f\n", 3.0, 2.0, 3.0/2.0); 
    printf("The remainder of the two numbers are : num1 = %d, num2 = %d, remainder = %d\n", 3, 2, 3%2);
    return 0;
}

//The above is my solution to the Milestone question.

//Answer. 

#include <stdio.h>
int main()
{
    printf("%d + %d = %d \n", 5, 2, 5+2);
    printf("%d - %d = %d \n", 5, 2, 5-2);
    printf("%d * %d = %d \n", 5, 2, 5*2);
    printf("%d / %d = %d \n", 5, 2, 5/2); // We take just the FULL part of the division
    printf("%d %% %d = %d \n", 5, 2, 5%2); // Taking the remainder. Think about what would happen if you used just one "%".
    return 0;
}


//That's the end of this section. 