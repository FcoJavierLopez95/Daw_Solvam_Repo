package _0001_Ejercicios_Java_21_10_2026;

import java.util.Scanner;

public class _0001_Ejercicios_Java_21_10_2026 {
    public static void main(String[] args) {
        // ------------------------------------------------------------------------------
        // todo EJERCICIO 1
        // Escribe un programa que pida por teclado un día de la semana y que diga
        // qué asignatura toca a primera hora ese día.
        // ------------------------------------------------------------------------------

        // Declaración de variables
        Scanner sc = new Scanner(System.in);
        int menu;
        String day="";

        // Es número entre 1 y 5?
        do {
            System.out.printf("Elige un día de la semana:%n1.- Lunes%n2.- Martes%n3.- Miércoles%n4.- Jueves%n5.- Viernes%n ");
            try {
                menu = sc.nextInt();

                switch (menu) {
                    case 1:
                        day = "Lunes";
                        break;
                    case 2:
                        day = "Martes";
                        break;
                    case 3:
                        day = "Miércoles";
                        break;
                    case 4:
                        day = "Jueves";
                        break;
                    case 5:
                        day = "Viernes";
                        break;
                    default:
                        System.out.println("introduce un valor entre 1 y 5");
                        break;
            }
            } catch (Exception exc) {
                System.out.println("Has introducido un valor no válido. Por favor inténtalo de nuevo:");
                menu = 0;
            }
            sc.nextLine();
        }while (menu < 1 || menu > 5);

        // Conclusión
        System.out.printf("Que te toca a primera hora el %s %n", day);
        String clas = sc.nextLine();
        System.out.printf("El %s tienes %s a primera hora.%n",day, clas);


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 2
        // Realiza un programa que pida una hora por teclado y que muestre luego
        // buenos días, buenas tardes o buenas noches según la hora. Se utilizarán
        // los tramos de 6 a 12, de 13 a 20 y de 21 a 5 respectivamente. Sólo se tienen
        // en cuenta las horas, los minutos no se deben introducir por teclado.
        // ------------------------------------------------------------------------------




        // ------------------------------------------------------------------------------
        // todo EJERCICIO 3
        // Calcula la nota de un trimestre de la asignatura Programación. El programa
        // pedirá las dos notas que ha sacado el alumno en los dos primeros controles.
        // Si la media de los dos controles da un número mayor o igual a 5, el alumno
        // está aprobado y se mostrará la media. En caso de que la media sea un número
        // menor que 5, el alumno habrá tenido que hacer el examen de recuperación que
        // se califica como apto o no apto, por tanto se debe preguntar al usuario
        // ¿Cuál ha sido el resultado de la recuperación? (apto/no apto). Si el resultado
        // de la recuperación es apto, la nota será un 5; en caso contrario, se mantiene
        // la nota media anterior.
        // Ejemplo 1:
        // 1 Nota del primer control: 7
        // 2 Nota del segundo control: 10
        // 3 Tu nota de Programación es 8.5
        // Ejemplo 2:
        // 1 Nota del primer control: 6
        // 2 Nota del segundo control: 3
        // 3 ¿Cuál ha sido el resultado de la recuperación? (apto/no apto): apto
        // 4 Tu nota de Programación es 5
        // Ejemplo 3:
        // 1 Nota del primer control: 6
        // 2 Nota del segundo control: 3
        // 3 ¿Cuál ha sido el resultado de la recuperación? (apto/no apto): no apto
        // 4 Tu nota de Programación es 4.5
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 4
        // Muestra los números múltiplos de 5 de 0 a 100 utilizando un bucle for,
        // un bucle while y un bucle do-while.
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 5
        // Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás
        // utilizando un bucle for, un bucle while y un bucle do-while.
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 6
        // Escribe un programa que calcule el precio final de un producto según su
        // base imponible (precio antes de impuestos), el tipo de IVA aplicado
        // (general, reducido o superreducido) y el código promocional. Los tipos de
        // IVA general, reducido y superreducido son del 21%, 10% y 4% respectivamente.
        // Los códigos promocionales pueden ser nopro, mitad, meno5 o 5porc que
        // significan respectivamente que no se aplica promoción, el precio se reduce
        // a la mitad, se descuentan 5 euros o se descuenta el 5%. El ejercicio se da
        // por bueno si se muestran los valores correctos, aunque los números no estén tabulados.
        // Ejemplo:
        // 1 Introduzca la base imponible: 25
        // 2 Introduzca el tipo de IVA (general, reducido o superreducido): reducido
        // 3 Introduzca el código promocional (nopro, mitad, meno5 o 5porc): mitad
        // 4 Base imponible 25.00
        // 5 IVA (10%) 2.50
        // 6 Precio con IVA 27.50
        // 7 Cód. promo. (mitad): -13.75
        // 8 TOTAL 13.75
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 7
        // Realiza el control de acceso a una caja fuerte. La combinación será un número
        // de 4 cifras. El programa nos pedirá la combinación para abrirla. Si no
        // acertamos, se nos mostrará el mensaje “Lo siento, esa no es la combinación”.
        // Si acertamos se nos dirá “La caja fuerte se ha abierto satisfactoriamente”.
        // Tendremos cuatro oportunidades para abrir la caja fuerte.
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 8
        // Realiza un programa que nos diga cuántos dígitos tiene un número introducido
        // por teclado.
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 9
        // Realiza un programa que sume los 100 números siguientes a un número entero
        // y positivo introducido por teclado. Se debe comprobar que el dato introducido
        // es correcto (que es un número positivo).
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 10
        // Escribe un programa que lea un número n e imprima una pirámide de números
        // con n filas como en la siguiente figura:
        // 1
        // 1 2 1
        // 1 2 3 2 1
        // 1 2 3 4 3 2 1
        // ------------------------------------------------------------------------------

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 11
        // Realiza un programa que pida un número por teclado y que luego muestre
        // ese número al revés.
        // ------------------------------------------------------------------------------
    }
}