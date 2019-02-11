%{

  #include<stdio.h>
  int numeroLineas =0, numeroCaracteres=0;

%}
%%
\n	{numeroLineas++; numeroCaracteres++;}
.	{numeroCaracteres++;}
%%
void main(){
  yylex();
  printf("# de Líneas: %d, # de caracteres: %d\n", 
	numeroLineas, numeroCaracteres
	);
}
