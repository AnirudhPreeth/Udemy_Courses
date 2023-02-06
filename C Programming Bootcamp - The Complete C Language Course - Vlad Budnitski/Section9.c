/*
Section 9: Variables & Data Types - From Zero To Hero!
*/

/*
Think of variables as boxes. Box type. Box name. Box content. Box address. 
Variable type. Variable name. Variable content. Variable address. 

Variable Declaration - Variable "creation".
<type><name>; -> int age; , double temp; (Example). 
<type of variable> <variable name>;

Assignment - Put some value in variable. 
To "assign" some value to a variable. Value that matches the type of the variable. 
int age; age = 30; (Example).

Reading Input from the User - Reading data from the user.
Define variables using assignment. 
int grade1; int grade2; grade1 = 80; grade2 = 100; printf("Average = %d\n", (grade1 + grade2)/2); (Example).
Using "Scanf". 
Example : int grade1; int grade2; scanf("%d", &grade1); scanf("%d", &grade1); printf("Average = %d\n", (grade1 + grade2)/2); 
Scanf - Reads the value which has been inserted into the console and %d as it's an integer. 
& - specifies all it does is to specify that the value read from the console using these percentages (%d), they should go and be placed at the address where grade one resides.

*/

//Variable Declaration. 

#include <stdio.h>
int main()
{
	int age;
	double temp;
	return 0;
}

//Variable - Assignments + Initialization. 

#include <stdio.h>
int main()
{
	int age;
	age = 30;
	double temp;
	temp = 26.5;
	return 0;
}

//Variables - Printing Variables and Expression. 

#include <stdio.h>

int main()
{
	int grade1;
	int grade2;
	grade1 = 80;
	grade2 = 100;
	printf("Average = %d\n", (grade1 + grade2) / 2);
	return 0;
}

//Variables - Reading Input from the User. 

#include <stdio.h>
int main()
{
	int grade1;
	int grade2;
	scanf("%d", &grade1);
	scanf("%d", &grade2);
	printf("Average = %d\n", (grade1 + grade2) / 2);
	return 0;
}

//Variable Code Example 1. 

#include <stdio.h>
int main()
{
	int num;
	scanf("%d", &num);
	printf("num is %d \n", num);
	return 0;
}

//& specifies the address. 
//Another.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int num;
	num = 10;
	printf("num is %d \n", num);
	return 0;
}

//Challenge #1 - Find your Year of Birth!

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int current_year, age, year_born;
	scanf("%d", &current_year);
	printf("Current year is %d\n", current_year);
	scanf("%d", &age);
	printf("Age is %d\n", age);
	year_born = current_year - age;
	printf("The year you were born is : %d\n", year_born);
	return 0;
}

//The above is my solution to the given problem. 

//Answer: 

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int currentYear, age;
	scanf("%d", &currentYear);
	scanf("%d", &age);
	printf("You were born in %d\n", currentYear - age); 
	return 0;
}

//Challenge #2 - Calculate Rectangle's Area.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int area, length, breadth;
	scanf("%d", &length);
	scanf("%d", &breadth);
	area = length * breadth;
	printf("The area of a rectangle is : %d", area);
	return 0;
} 

#include <stdio.h>
#include <stdlib.h>
int main()
{
	double area, length, breadth;
	printf("Length is : ");
	scanf("%lf", &length);
	printf("Breadth is : ");
	scanf("%lf", &breadth);
	area = length * breadth;
	printf("The area of a rectangle is : %lf", area);
	return 0;
}

//The above is my solution to the given problem. 

//Answer:

#include <stdio.h>
#include <stdlib.h>
int main()
{
	double area, length, breadth;
	printf("Length is : ");
	scanf("%lf", &length);
	printf("Breadth is : ");
	scanf("%lf", &breadth);
	area = length * breadth;
	printf("The area of a rectangle is : %lf", area);
	return 0;
}

//Assignment: Practical Assignment: Calculate Rectangle's Perimeter.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	float length, breadth, area;
	printf("Enter the length : ");
	scanf("%f", &length);
	printf("Enter the breadth: ");
	scanf("%f", &breadth);
	area = length * breadth;
	printf("The area of the rectangle is : %f", area);
	return 0;
}

//Made a mistake. Calculated area instead of perimeter. 

#include <stdio.h>
#include <stdlib.h>
int main()
{
	float length, breadth, perimeter;
	printf("Enter the length : ");
	scanf("%f", &length);
	printf("Enter the breadth: ");
	scanf("%f", &breadth);
	perimeter = 2 *(length + breadth);
	printf("The perimeter of the rectangle is : %f", perimeter);
	return 0;
}

//Final answer.

/*
Casting -
<type1> (any operation) <type1> = <type1. But that's not always the case. 
Example : 
5     /   2   =  2        OR   5   /  2    = 2.5
(int)  (int)   (int)          (int)  (int)  (double)
The result of the same mathematical operation can give two different results based on type itself.

*/

//Example. 

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int num1 = 5, num2 = 2;
	int result;
	result = num1/num2; //Assuming num2 != 0. 
	printf("Result = %d\n",result);
	return 0;
}

//Result is 2. 
//Now if we change result from int to double...

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int num1 = 5, num2 = 2;
	double result;
	result = num1/num2; //Assuming num2 != 0. 
	printf("Result = %f\n",result);
	return 0;
}

/*
Result is 2.00000.
It is 2.0 because as num1 and num2 are integers. 
Rule 1: When you mathematical operation between two numbers of the same type, the result you will get by default it will be... 
...actually of the same particular type. 
Implicit casting - Because casting is done behind the scenes and we don't explicitly say that we want to do type conversion. 
Rule 2: When you make a mathematical notation between an integer or a floating point number the result of operation would... 
...always be treated as it would have been done between two floating points.
Meaning result would be of a floating point number. 
*/

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int num1 = 5;
	double num2 = 2.0;
	double result;
	result = num1/num2; //Assuming num2 != 0. 
	printf("Result = %lf\n",result);
	return 0;
}

//Now the answer is 2.5000.

//Now, if we cast...(specify the type of the casting). 

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int num1 = 5;
	double num2 = 2.0;
	double result;
	result = num1/(double)num2; //Assuming num2 != 0. 
	printf("Result = %lf\n",result);
	return 0;
}

//Result will be 2.5000. 
//Can be used on num1 also. They were just casted on that one line. 

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int num1 = 5, num2 = 2;
	double result;
	result = (double)num1/(double)num2; //Assuming num2 != 0. 
	printf("Result = %lf\n",result);
	return 0;
}

//Result is 2.5000.
//You can cast a floating point into an integer or whatever type casting you wish. 

//Challenge #3 - Calculating your Average Grade.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	double English, Math, Science, Average;
	printf("Enter you Math grade: ");
	scanf("%lf", &Math);
	printf("Enter you Science grade: ");
	scanf("%lf", &Science);
	printf("Enter your English grade: ");
	scanf("%lf", &English);
	Average = (int)Math+(int)Science+(int)English / (int)3;
	printf("Your Average score is: %lf", Average);
	return 0;
}

//The above is my solution to the given problem. 

//Answer:

#include <stdio.h>
#include <stdlib.h>
int main()
{
	
}







