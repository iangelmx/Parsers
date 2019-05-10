/* Infix notation calculator.  */

%{
#include <math.h>
#include <stdio.h>
int yylex (void);
void yyerror (char const *error) {printf("%s <- Error",error);}
%}

/* Bison declarations.  */
%define api.value.type {double}
%token NUM
%left '-' '+'
%left '*' '/'
%precedence NEG   /* negation--unary minus */
%right '^'        /* exponentiation */

%% /* The grammar follows.  */
input: %empty
| input line { /*printf("Vi una linea");*/}
;

line:
'\n'
| exp '\n'  { printf ("\t R = %.10g ;\n", $1); }
;

exp:
NUM                { $$ = $1;           }
| exp '+' exp        { $$ = $1 + $3;  /*printf("Vi una suma");*/    }
| exp '-' exp        { $$ = $1 - $3;      }
| exp '*' exp        { $$ = $1 * $3;      }
| exp '/' exp        { $$ = $1 / $3;      }
| '-' exp  %prec NEG { $$ = -$2;          }
| exp '^' exp        { $$ = pow ($1, $3); }
| '(' exp ')'        { $$ = $2;           }
;
%%
int main(){
    return yyparse();
}