D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*

%{
#include<stdio.h>
%}

%%
"/*"			    { printf( "<p class=\"startComment\">%s</p>", yytext ); }

"auto"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"break"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"case"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"char"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"const"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"continue"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"default"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"do"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"double"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"else"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"enum"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"extern"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"float"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"for"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"goto"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"if"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"int"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"long"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"register"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"return"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"short"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"signed"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"sizeof"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"static"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"struct"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"switch"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"typedef"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"union"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"unsigned"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"void"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"volatile"		    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }
"while"			    { printf( "<p class=\"palabraRes\">%s</p>", yytext ); }

{L}({L}|{D})*		{ printf( "<p class=\"ids\">%s</p>", yytext ); }

0[xX]{H}+{IS}?		{ printf( "<p class=\"hexad\">%s</p>", yytext ); }
0{D}+{IS}?		    { printf( "<p class=\"octal\">%s</p>", yytext ); }
{D}+{IS}?		    { printf( "<p class=\"literal\">%s</p>", yytext ); }
L?'(\\.|[^\\'])+'	{ printf( "<p class=\"estiloX\">%s</p>", yytext ); }

{D}+{E}{FS}?		{ printf( "<p class=\"literal\">%s</p>", yytext ); }
{D}+"."             { printf( "<p class=\"estiloY\">%s</p>", yytext ); }

L?\"(\\.|[^\\"])*\"	{ printf( "<p class=\"estiloZ\">%s</p>", yytext ); }

"..."			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
">>="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"<<="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"+="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"-="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"*="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"/="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"%="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"&="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"^="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"|="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
">>"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"<<"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"++"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"--"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"->"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"&&"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"||"			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"<="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
">="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"=="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
"!="			{ printf( "<p class=\"ops\">%s</p>", yytext ); }
";"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
("{"|"<%")      { printf( "<p class=\"separador\">%s</p>", yytext ); }
("}"|"%>")      { printf( "<p class=\"separador\">%s</p>", yytext ); }
","			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
":"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"="			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"("			    { printf( "<p class=\"separador\">%s</p>", yytext ); }
")"			    { printf( "<p class=\"separador\">%s</p>", yytext ); }
("["|"<:")      { printf( "<p class=\"ops\">%s</p>", yytext ); }
("]"|":>")      { printf( "<p class=\"ops\">%s</p>", yytext ); }
"."			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"&"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"!"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"~"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"-"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"+"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"*"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"/"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"%"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"<"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
">"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"^"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"|"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }
"?"			    { printf( "<p class=\"ops\">%s</p>", yytext ); }

[ \t\v\f]		{ printf( "<p class=\"escapedChar\">%s</p>", yytext ); }
[\n]		{ printf( "<br>" ); }
.			    { printf( "<p class=\"char\">%s</p>", yytext ); }

%%

int main(void){
    printf("<html>");
    printf("<head><title>Sample page</title><link rel =  'stylesheet' type = 'text/css' href = 'styles.css' /></head> <body>");
    yylex();
    printf("</body></html>");
}