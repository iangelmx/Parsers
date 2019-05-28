%{
#include <stdlib.h>
#include "mfcalc.tab.h"
#include "tabla.h"
%}

%%
[0-9]+"."[0-9]+         { yylval.NUM = atof(yytext); return NUM;  }
[0-9]+                  { yylval.NUM = atoi(yytext); return NUM;  }
[a-zA-Z]+            { 
                        symrec *s;
                        s = getsym(yytext);
                        printf("Entré a azAz09 : %s\n\n", yytext);
                            if(s == 0){ //no existe la variable
                                printf("No encontró a >%s<", yytext);
                                s = putsym (yytext, VAR);
                                printf("\nse agregó la variable %s a la tabla de símbolos\n", yytext);
                            }
                            else{
                                printf("Encontró a >%s< en la tabla de símbolos\n", yytext);
                            }
                            yylval.VAR = s;
                            return s->type;
                    }
\n                      { return '\n'; }
[ ]
[-n+*/^=()]                { return *yytext; }


%%
