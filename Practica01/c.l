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
"/*"			    { printf( "<span class=\"startComment\">%s</span>", yytext ); }

"auto"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"break"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"case"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"char"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"const"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"continue"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"default"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"do"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"double"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"else"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"enum"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"extern"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"float"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"for"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"goto"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"if"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"int"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"long"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"register"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"return"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"short"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"signed"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"sizeof"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"static"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"struct"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"switch"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"typedef"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"union"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"unsigned"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"void"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"volatile"		    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }
"while"			    { printf( "<span class=\"palabraRes\">%s</span>", yytext ); }

{L}({L}|{D})*		{ printf( "<span class=\"ids\">%s</span>", yytext ); }

0[xX]{H}+{IS}?		{ printf( "<span class=\"hexad\">%s</span>", yytext ); }
0{D}+{IS}?		    { printf( "<span class=\"octal\">%s</span>", yytext ); }
{D}+{IS}?		    { printf( "<span class=\"literal\">%s</span>", yytext ); }
L?'(\\.|[^\\'])+'	{ printf( "<span class=\"estiloX\">%s</span>", yytext ); }

{D}+{E}{FS}?		{ printf( "<span class=\"literal\">%s</span>", yytext ); }
{D}+"."             { printf( "<span class=\"estiloY\">%s</span>", yytext ); }

L?\"(\\.|[^\\"])*\"	{ printf( "<span class=\"estiloZ\">%s</span>", yytext ); }

"..."			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
">>="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"<<="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"+="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"-="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"*="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"/="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"%="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"&="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"^="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"|="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
">>"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"<<"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"++"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"--"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"->"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"&&"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"||"			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"<="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
">="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"=="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
"!="			{ printf( "<span class=\"ops\">%s</span>", yytext ); }
";"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
("{"|"<%")      { printf( "<span class=\"separador\">%s</span>", yytext ); }
("}"|"%>")      { printf( "<span class=\"separador\">%s</span>", yytext ); }
","			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
":"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"="			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"("			    { printf( "<span class=\"separador\">%s</span>", yytext ); }
")"			    { printf( "<span class=\"separador\">%s</span>", yytext ); }
("["|"<:")      { printf( "<span class=\"ops\">%s</span>", yytext ); }
("]"|":>")      { printf( "<span class=\"ops\">%s</span>", yytext ); }
"."			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"&"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"!"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"~"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"-"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"+"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"*"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"/"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"%"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"<"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
">"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"^"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"|"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }
"?"			    { printf( "<span class=\"ops\">%s</span>", yytext ); }

[ \v\f]		{ printf( "<span class=\"escapedChar\">%s</span>", yytext ); }
[\t]		{ printf( "&nbsp;&nbsp;&nbsp;&nbsp;" ); }
[\n]		{ printf( "<br/>" ); }
.			    { printf( "<span class=\"char\">%s</span>", yytext ); }

%%

int main(void){
    printf("<html>");
    printf("<head><title>Sample page</title><link rel =  'stylesheet' type = 'text/css' href = 'styles.css' /></head> <body>");
    yylex();
    printf("</body></html>");
}