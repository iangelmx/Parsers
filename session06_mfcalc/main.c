#include "tabla.h"

/* Called by yyparse on error.  */
void
yyerror (char const *s)
{
  //fprintf (stderr, "%s\n", s);
  printf("Hubo un error: %s\n", s);
}

int
main (int argc, char const* argv[])
{
  int i;
  /* Enable parse traces on option -p.  */
  for (i = 1; i < argc; ++i)
    if (!strcmp(argv[i], "-p"))
        yydebug = 1;
  init_table ();
  return yyparse ();
}