%{
/* need this for the call to atof() below */
#include <math.h>
%}

DIGIT    [0-9]
ID       [a-z][a-z0-9]*

%%

{DIGIT}+    {
     printf( "Un entero: %s (%d)\n", yytext,
             atoi( yytext ) );
     }

{DIGIT}+"."{DIGIT}*        {
     printf( "Un flotante: %s (%g)\n", yytext,
             atof( yytext ) );
     }

if|then|begin|end|procedure|function        {
     printf( "Una palabra reservada: %s\n", yytext );
     }

{ID}        printf( "Un identificador: %s\n", yytext );

"+"|"-"|"*"|"/"   printf( "Un operador: %s\n", yytext );

"{"[^{}\n]*"}"     /* eat up one-line comments */

[ \t\n]+          /* eat up whitespace */

.           printf( "Caracter desconocido :v : %s\n", yytext );

%%
int main( int argc, char **argv )
{
++argv, --argc;  /* skip over program name */
if ( argc > 0 )
     yyin = fopen( argv[0], "r" );
else
     yyin = stdin;

yylex();
}
