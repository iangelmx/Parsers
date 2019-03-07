/* Calculadora de notación polaca inversa. */

%{
#define YYSTYPE double
#include <math.h>
%}

%token NUM

%% /* A continuación las reglas gramaticales y las acciones */
input:    /* vacío */
        | input line
;

line:     '\n'
        | exp '\n'  { printf ("\t%.10g\n", $1); }
;

exp:      NUM             { $$ = $1;         }
        | exp exp '+'     { $$ = $1 + $2;    }
        | exp exp '-'     { $$ = $1 - $2;    }
        | exp exp '*'     { $$ = $1 * $2;    }
        | exp exp '/'     { $$ = $1 / $2;    }
      /* Exponenciación */
        | exp exp '^'     { $$ = pow ($1, $2); }
      /* Menos unario   */
        | exp 'n'         { $$ = -$1;        }
;
%%