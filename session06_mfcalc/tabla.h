#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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

struct init
{
  char const *fname;
  double (*fnct) (double);
};

extern struct init const arith_fncts[];
extern int yydebug;
/* The symbol table: a chain of 'struct symrec'.  */
extern symrec *sym_table;
extern symrec *putsym (char const *, int);
extern symrec *getsym (char const *);

/* Put arithmetic functions in table.  */
 
void
init_table (void);
#endif
