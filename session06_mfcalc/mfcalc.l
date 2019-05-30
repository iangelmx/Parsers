%{
#include<stdlib.h>
#include <math.h>
#include "tabla.h"
#include "mfcalc.tab.h"
%}


%%

[0-9]+"."[0-9]+         { yylval.NUM = atof(yytext); return NUM;  }
[0-9]+                  { yylval.NUM = atoi(yytext); return NUM;  }
\n                      { return '\n'; }
[ ]
"if"                    { /*printf("Vi un if \n");*/ return IF; }
"then"                  { /*printf("Vi un then \n");*/ return THEN; }
"endif"               { /*printf("Vi un fin-si \n");*/ return FINIF;}

[a-zA-Z]+            { 
                            symrec *s = getsym (yytext);
                            if (!s){
                                //printf("No encontró a >%s<", yytext);
                                s = putsym (yytext, VAR);
                            }
                            else{
                                //printf("Encontró a >%s< en la symbol table\n", yytext);
                            }
                            yylval.VAR = s; /* or yylval.FUN = s. */
                            //printf("s type: %d\n", VAR);
                            return s->type;
                        }
[-n+*/^=(){}]                { return *yytext; }

%%
