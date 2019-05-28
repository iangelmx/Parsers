%{
#include<stdlib.h>
#include <math.h>
#include "tabla.h"
#include "mfcalc.tab.h"
%}


%%
[0-9]+"."[0-9]+         { yylval.NUM = atof(yytext); return NUM;  }
[0-9]+                  { yylval.NUM = atoi(yytext);     return NUM;  }
\n                      { return '\n'; }
"SIN"                  { yylval.NUM = 1; return TFUNC; }
"COS"                  { yylval.NUM = 2; return FNCT; }
"TAN"                  { yylval.NUM = 3; return FNCT; }

[ ]
[-n+*/^]                { return *yytext; }

%%
