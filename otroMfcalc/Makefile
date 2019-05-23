run : a.out
	./a.out -p
clean : 
	rm *.o mfcalc.tab.h mfcalc.tab.c a.out lex.yy.c

mfcalc.tab.c : mfcalc.y
	bison -d mfcalc.y

mfcalc.tab.h: mfcalc.tab.c

tabla.o : tabla.c
	gcc -c tabla.c

	
mfcalc.tab.o : mfcalc.tab.c
	gcc -c mfcalc.tab.c

main.o: main.c
	gcc -c main.c

a.out : mfcalc.tab.o
	gcc mfcalc.tab.o -lm -ll