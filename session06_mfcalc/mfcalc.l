%{
#include<stdlib.h>
#include "calc.h"
#include "mfcalc.tab.h"
%}


%%
[0-9]+"."[0-9]+ { yylval = (yytext); return NUM;}
\n              { return '\n'; }
[ ]
[-n+*/^]              { return *yytext; }

%%
