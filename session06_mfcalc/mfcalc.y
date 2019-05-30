%{
#include <stdio.h>  /* For printf, etc. */
#include <math.h>   /* For pow, used in the grammar.  */
#include "tabla.h"   /* Contains definition of 'symrec'.  */
int yylex (void);
void yyerror (char const *error) {printf("%s\t<- Error\n\n",error);}
void
init_table (void);
%}

%define api.value.type union /* Generate YYSTYPE from these types:  */

%token <double>  NUM         /* Simple double precision number.  */
%token <symrec*> VAR FNCT    /* Symbol table pointer: variable and function.  */
%token <int> IF FINIF THEN
%type  <double>  exp
%type  <double>  selection_statement
%type  <double>  exp_list


%precedence '='
%left '-' '+'
%left '*' '/'
%precedence NEG /* negation--unary minus */
%right '^'      /* exponentiation */
%% /* The grammar follows.  */
input:
%empty
| input line
;

line:
'\n'
| exp '\n'   { printf ("R = %.10g ;\n", $1); }
| error '\n' { yyerrok;                }
| selection_statement { printf ("Rif = %.10g ;\n", $1); }
;

exp_list:
exp '\n'
|exp_list exp '\n'
;

selection_statement:
IF exp THEN exp_list FINIF { printf("exp-> %g", $2); 
                        if( $2 == 1){
                          
                          $$ = $4;
                        }else{
                          $$ = -99;
                        }
                      }
|IF exp THEN '\n' exp_list '\n' FINIF { printf("exp-> %g", $2); 
                                  if( $2 == 1){
                                    
                                    $$ = $5;
                                  }else{
                                    $$ = -99;
                                  }
                                }
;

exp:
NUM                { $$ = $1;                         }
| VAR                { $$ = $1->value.var;            }
| VAR '=' exp        { $$ = $3; $1->value.var = $3;      }
| FNCT '(' exp ')'   { $$ = (*($1->value.fnctptr))($3);  }
| exp '+' exp        { $$ = $1 + $3;  /*printf("$1->%g $3->%g | ", $1, $3);*/                  }
| exp '-' exp        { $$ = $1 - $3;  /*printf("%g %g", $1, $3);*/                  }
| exp '*' exp        { $$ = $1 * $3;                    }
| exp '/' exp        { $$ = $1 / $3;                    }
| '-' exp  %prec NEG { $$ = -$2;                        }
| exp '^' exp        { $$ = pow ($1, $3);               }
| '(' exp ')'        { $$ = $2;                         }
| exp '=' '=' exp    { $$ = $1 == $4; }
| VAR '=' '=' exp    { $$ = $1->value.var == $4; }
;
/* End of grammar.  */
%%
void
init_table (void);
int yydebug;

int main (int argc, char const* argv[])
{
  int i;
  /* Enable parse traces on option -p.  */
  for (i = 1; i < argc; ++i)
    if (!strcmp(argv[i], "-p"))
       yydebug = 1;
       init_table ();
    return yyparse ();
}