%{
#include <stdio.h>  /* For printf, etc. */
#include <math.h>   /* For pow, used in the grammar.  */
#include <stdlib.h>
#include <string.h>
#include "tabla.h"   /* Contains definition of 'symrec'.  */
int yylex (void);
int yydebug;
static void init_table(void);
//void yyerror (char const *error) {printf("%s\t<- Error",error);}
%}

%code requires
{
	#include "tabla.h"
}

%define api.value.type union /* Generate YYSTYPE from these types:  */
%token <double>  NUM         /* Simple double precision number.  */
%token <symrec*> VAR FNCT    /* Symbol table pointer: variable and function.  */
%type  <double>  exp

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
;


exp:
  NUM                { $$ = $1;                         }
| VAR                { $$ = $1->value.var;       }
| VAR '=' exp        { $$ = $3; $1->value.var = $3;     }
| FNCT '(' exp ')'   { $$ = (*($1->value.fnctptr))($3); }
| exp '+' exp        { $$ = $1 + $3;  /*printf("$1->%g $3->%g | ", $1, $3);*/                  }
| exp '-' exp        { $$ = $1 - $3;  /*printf("%g %g", $1, $3);*/                  }
| exp '*' exp        { $$ = $1 * $3;                    }
| exp '/' exp        { $$ = $1 / $3;                    }
| '-' exp  %prec NEG { $$ = -$2;                        }
| exp '^' exp        { $$ = pow ($1, $3);               }
| '(' exp ')'        { $$ = $2;                         }
;
/* End of grammar.  */
%%

static void init_table (void){
  int i;
  for (i = 0; arith_fncts[i].fname != 0; i++){
    symrec *ptr = putsym (arith_fncts[i].fname, FNCT);
    //symrec *ptr = putsym (arith_fncts[i].fname, 260);
    ptr->value.fnctptr = arith_fncts[i].fnct;
  }
}


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