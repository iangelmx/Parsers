#ifndef calc
#define calc
/* Function type.  */
typedef double (*func_t) (double);

/* Data type for links in the chain of symbols.  */
struct symrec
{
    char *name;  /* name of symbol */
    int type;    /* type of symbol: either VAR or FNCT */
    union
    {
        double var;      /* value of a VAR */
        func_t fnctptr;  /* value of a FNCT */
    } value;
    struct symrec *next;  /* link field */
};

typedef struct symrec symrec;

/* The symbol table: a chain of 'struct symrec'.  */
extern symrec *sym_table;


symrec *putsym (char const *, int);
symrec *getsym (char const *);

int FNCT = 0;

struct init
{
    char const *fname;
    double (*fnct) (double);
};

float atan(){
    return 1.0;
}

static float cos(){
    return 2.0;
}

static float sin(){
    return 3.0;
}

static float exp(){
    return 4.0;
}

static float log(){
    return 5.0;
}

static float sqrt(){
    return 6.0;
}

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
    for (i = 0; arith_fncts[i].fname != 0; i++){
        symrec *ptr = putsym (arith_fncts[i].fname, FNCT);
        ptr->value.fnctptr = arith_fncts[i].fnct;
    }
}

#endif