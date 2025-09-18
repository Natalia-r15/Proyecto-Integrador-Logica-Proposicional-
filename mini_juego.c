#include <stdio.h>
#include <time.h> //para temporizador

int main() {
    printf("Hola usuario!, bienvenido al minijuego\n");
    char jugador1[20], jugador2[20];
    
    printf("Jugador 1, ingrese su nombre: ");
    scanf("%s", jugador1);
    printf("Jugador 2, ingrese su nombre: ");
    scanf("%s", jugador2);

    int op1, op2, op3;
    //bloque 1
    printf("\n%s, arma tu proposición\n", jugador1);
    printf("Elige un operador para el primer bloque (p ? q)\n");
    printf("1. AND (p && q)\n2. OR (p || q)\n3. NOT (!p)\n");
    scanf("%d", &op1);

    //bloque 2
    printf("Elige un operador para el segundo bloque (r ? s)\n");
    printf("1. AND (r && s)\n2. OR (r || s)\n3. NOT (!r)\n");
    scanf("%d", &op2);

    //combinación de bloques
    printf("Elige un operador para combinar ambos bloques (bloque1 ? bloque2)\n");
    printf("1. AND (bloque1 && bloque2)\n2. OR (bloque1 || bloque2)\n");
    scanf("%d", &op3);

    //turno del jugador 2
    printf("\nAhora es el turno de %s\n", jugador2);
    printf("Tienes 3 minutos para descifrar la proposición.\n");

    time_t inicio, actual;
    time(&inicio);  //inicia el temporizador

    int intentos = 0, gano = 0;
    //variable gano para verificar si ganó y salir del ciclo

    while(1) {  //se ejecuta infinitamente hasta que se cumpla una condición de salida (1)
        time(&actual);  //captura el tiempo actual
        double transcurrido = difftime(actual, inicio); //difftime calcula la diferencia en segundos entre dos tiempos
        if(transcurrido >= 180) { //si se exceden los 3 minutos se termina el juego
            printf("\nSe acabó el tiempo! %s gana!\n", jugador1);
            break;
        }

        int p, q, r, s, valor;

        //pedir p
        do {
            printf("\nIngresa el valor de p (0 o 1): ");
            scanf("%d", &valor);
            if(valor == 0 || valor == 1) p = valor; //si el valor ingresado es correcto, se almacena en p
            else printf("Valor inválido! Debe ser 0 o 1.\n");
        } while(valor != 0 && valor != 1);  //no sale del ciclo hasta que el usuario ingrese 0 o 1

        //pedir q
        do {
            printf("Ingresa el valor de q (0 o 1): ");
            scanf("%d", &valor);
            if(valor == 0 || valor == 1) q = valor;
            else printf("Valor inválido! Debe ser 0 o 1.\n");
        } while(valor != 0 && valor != 1);

        //pedir r
        do {
            printf("Ingresa el valor de r (0 o 1): ");
            scanf("%d", &valor);
            if(valor == 0 || valor == 1) r = valor;
            else printf("Valor inválido! Debe ser 0 o 1.\n");
        } while(valor != 0 && valor != 1);

        //pedir s
        do {
            printf("Ingresa el valor de s (0 o 1): ");
            scanf("%d", &valor);
            if(valor == 0 || valor == 1) s = valor;
            else printf("Valor inválido! Debe ser 0 o 1.\n");
        } while(valor != 0 && valor != 1);

        //evaluar bloques
        int bloque1 = (op1 == 1) ? (p && q) : (op1 == 2) ? (p || q) : (!p);
        //si la opción es 1 es AND, si es 2 es OR, si es 3 es NOT
        int bloque2 = (op2 == 1) ? (r && s) : (op2 == 2) ? (r || s) : (!r);

        //combinar bloques
        int resultado = (op3 == 1) ? (bloque1 && bloque2) : (bloque1 || bloque2);

        intentos++; //incrementa el número de intentos
        printf("Resultado de la proposición: %d (%d intentos, %.0f segundos transcurridos)\n", resultado, intentos, transcurrido);

        if(resultado == 1) {
            printf("\nFelicidades %s, has descifrado la proposición!\n", jugador2);
            printf("Total de intentos: %d\n", intentos);
            printf("Tiempo utilizado: %.0f segundos\n", transcurrido);
            gano = 1;   //si ganó, el valor de la variable cambia a 1 y sale del ciclo
            break;
        }
    }

    return 0;
}
