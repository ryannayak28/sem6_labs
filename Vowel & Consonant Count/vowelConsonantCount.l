
%{
	#include<stdio.h>
	int Vowel=0;
	int Consonant=0;
%}

%%
[aeiouAEIOU] {printf("Vowels\t\n"); Vowel++;}
[a-zA-Z] {printf("Consonants\t\n"); Consonant++;}
\n    {printf("Vowels=%d and Consonants=%d", Vowel, Consonant);}
%%

int yywrap()
{
	return 1;
}

int main()
{
	printf("Enter a string\n");
	yylex();
	return 0;
}