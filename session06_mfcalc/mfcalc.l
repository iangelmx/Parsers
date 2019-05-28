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
"sin"                  { yylval.NUM = 1; return TFUNC; }
"cos"      {
                             
                            printf("Entré a cos : %s\n\n", yytext);
                            symrec *s = getsym (yytext);
                            if (!s){
                                printf("No encontró a coseno");
                                s = putsym (yytext, VAR);
                            }
                            else{
                                printf("Encontró a coseno en la symbol table\n");
                            }
                            yylval.NUM = 15;

                            yylval.FNCT = s; /* or yylval.FUN = s. */
                            printf("s type: %d\n", s->type);
                            return FNCT;
                            
                        }
"TAN"                  { yylval.NUM = 3; return FNCT; }
[ ]
[-n+*/^]                { return *yytext; }

[a-zA-Z0-9]+            { 
                        printf("Entré a azAz09 : %s\n\n", yytext);
                            symrec *s = getsym (yytext);
                            if (!s){
                                printf("No encontró a >%s<", yytext);
                                s = putsym (yytext, VAR);
                            }
                            else{
                                printf("Encontró a >%s< en la symbol table\n", yytext);
                            }
                            yylval.VAR = s; /* or yylval.FUN = s. */
                            printf("s type: %d\n", VAR);
                            return VAR;
                        }

%%
