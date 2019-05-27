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

[ ]
[-n+*/^]                { return *yytext; }

%%
