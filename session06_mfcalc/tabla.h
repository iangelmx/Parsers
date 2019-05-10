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

symrec *putsym (char const *, int);
symrec *getsym (char const *);

float atan(){
    return 0;
}
float cos(){
    return 0;
}
float exp(){
    return 0;
}
float log(){
    return 0;
}
float sin(){
    return 0;
}
float sqrt(){
    return 0;
}


struct init
{
  char const *fname;
  double (*fnct) (double);
};

struct init const arith_fncts[] =
{
  { "atan", atan },
  { "cos",  cos  },
  { "exp",  exp  },
  { "ln",   log  },
  { "sin",  sin  },
  { "sqrt", sqrt },
  { 0, 0 },
};

/* The symbol table: a chain of 'struct symrec'.  */
symrec *sym_table;

/* Put arithmetic functions in table.  */
static
void
init_table (void)
{
  int i;
  for (i = 0; arith_fncts[i].fname != 0; i++)
    {
 symrec *ptr = putsym (arith_fncts[i].fname, FNCT);
 ptr->value.fnctptr = arith_fncts[i].fnct;
    }
}
#endif