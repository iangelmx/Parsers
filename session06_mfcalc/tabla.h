#include <stdlib.h> /* malloc. */
#include <string.h> /* strlen. */
#include <math.h>
#include <stdio.h>



#ifndef __TABLA_H__
#define __TABLA_H__
/* Function type.  */
typedef double (*func_t) (double);

/* Data type for links in the chain of symbols.  */
struct symrec
{
  char *name;  /* name of symbol */
  int type;    /* type of symbol: either VAR or FNCT */
  union
  {
    double var; /* value of a VAR */
    func_t fnctptr;  /* value of a FNCT */
  } value;
  struct symrec *next;  /* link field */
};

typedef struct symrec symrec;

/* The symbol table: a chain of 'struct symrec'.  */
extern symrec *sym_table;
//extern symrec *FNCT;


////>>>
extern int yydebug;
//extern YYSTYPE yylval;

symrec *putsym (char const *, int);
symrec *getsym (char const *);

struct init
{
  char const *fname;
  double (*fnct) (double);
};


/* Put arithmetic functions in table.  */
void
init_table (void);
#endif
