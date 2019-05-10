%{
#include<stdlib.h>
#include "infix_calc.tab.h"
%}


%%
[0-9]+"."[0-9]+ { yylval = atof(yytext); return NUM;}
\n              { /*printf("Regresa un enter");*/ return '\n'; }
[ ]
[-n+*/^]              { return *yytext; }
%%
