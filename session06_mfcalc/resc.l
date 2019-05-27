%{
#include<stdlib.h>
#include <math.h>
//#include "tabla.h"
//#include "mfcalc.tab.h"
%}


%%
[0-9]+"."[0-9]+         { yylval = atof(yytext); printf(typeof(*yytext)); return NUM;  }
[0-9]+                  { yylval = atoi(yytext); printf(typeof(*yytext)); return NUM;  }
\n                      { return '\n'; }
[ ]
[-n+*/^]                { return *yytext; }

[a-zA-Z]+               { yylval.VAR = yytext; return VAR; }
"sin"                   { yylval.FNCT = yytext; return FNCT; }
"cos"                   { yylval.FNCT = yytext; return FNCT; }
"tan"                   { yylval.FNCT = yytext; return FNCT; }

%%
