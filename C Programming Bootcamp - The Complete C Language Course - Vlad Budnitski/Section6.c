/* 
Section 6: Welcome First Program. 
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    //Your code comes here. 
    //Your code comes here.
    //Your code comes here.
    return 0;
}

/*
int main() - Entry point. 
It's sort of a container for a block of commands. 
And this block of commands is specified by brackets - {}.
{ - Beginning, } - End.

#include <stdio.h>
#include <stdlib.h>
They allow you to include different functionalities in your program. "Stdio" stands for Standard Input-Output.
It just gives us necessary funtionality to work with inputs such as reading information from the keyboard, and also to work with outputs such as displaying things on the screen. 
return 0;
Just a command indicating that this code, has finished running sucessfully. 
Basically, when your operating system executes a program and the returned value is zero, the operating system can assume that the program has terminated successfully.
Every command in C ends with a semicolon. 
*/

//Welcome printf() function program. 

#include <stdio.h>
int main()
{
    printf("Hello World!\n");
    printf("Hello Alpha Tech!\n");
    printf("1234567\n");
    printf("Hello\n Alpha\n Tech \n!");
    printf("Hello  \n Alpha \n Tech!\n");
    return 0;
}

/*
printf() - Print out what we want on screen. 
Specify the string that we want to see in our screen. Between the quotation marks. 
Don't have to use words. You can also use numbers as well. And run them. 
Specify getting one line down by using "\n" notation within the printf command. 
You can add \n where ever you wish in the text. 
*/

// Challenge #1 - Print Your First Name And Last Name!

#include <stdio.h>
int main()
{
    printf("Anirudh\n");
    printf("Preeth\n");
    printf("Anirudh Preeth");
    return 0;
}

//The above is my solution to the given question. 

//Answer:

#include <stdio.h>
int main()
{
    printf("Bill Clinton\n");
    printf("Bill \nClinton\n");
    printf("First Name: Bill \nLast Name: Clinton");
    return 0;
}

//Challenge #2 - Print Your Full Name, Age, And Gender!

#include <stdio.h>
int main()
{
    printf("Name : Anirudh Preeth\n");
    printf("Full Name : Anirudh Parole Preeth\n");
    printf("Age : 21\n");
    printf("Gender : Male\n");
    
    printf("\nName : Anirudh Preeth \nFull Name : Anirudh Parole Preeth \nAge : 21 \nGender : Male");
    return 0;
}

//The above is my solution to the given question. 

//Answer:

#include <stdio.h>
int main()
{
    printf("Full Name : Brad Pitt\n");
    printf("Age : 55\n");
    printf("Gender : Male\n");
    printf("Full Name : Brad Pitt\nAge : 55\nGender :Male\n");
    return 0;
}

//Challenge #3 - Print An "Isosceles Triangle".

#include <stdio.h>
int main()
{
    printf("  *\n");
    printf(" ***\n");
    printf("*****\n");
    printf("  *\n ***\n*****\n");
    return 0;
}

//The above is my solution to the given question. 

//Answer:

#include <stdio.h>
int main()
{
    printf("  *\n");
    printf(" *** \n");
    printf("*****\n");
    printf("  *  \n *** \n*****\n");
    return 0;
}

//That's the end of this section. 