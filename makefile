CC=gcc
CFLAGS=-Wall -O2
LIBS=-lX11 -lXxf86vm -lpthread

all: moteur_muscle

moteur_muscle: moteur_muscle.c
	$(CC) $(CFLAGS) moteur_muscle.c -o moteur_muscle $(LIBS)

clean:
	rm -f moteur_muscle