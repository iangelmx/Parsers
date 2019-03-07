%{
#include<stdlib.h>
#include "rpcalc.tab.h"
%}


%%
[0-9]+"."[0-9]+ { yylval = atof(yytext); return NUM;}
\n              { return '\n'; }
[ ]
[-n+*/^]              { return *yytext; }
%%
