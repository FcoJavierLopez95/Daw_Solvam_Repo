package _0001_Ejercicios_Java_21_10_2026;

import java.util.Scanner;

public class _001_Ejercicios_Java_1_21_10_2026 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // ------------------------------------------------------------------------------
        //  EJERCICIO 1
        // Escribe un programa que muestre tu nombre por pantalla.
        // ------------------------------------------------------------------------------

        String name;

        System.out.println("Dime tu nombre:");
        name = sc.nextLine();

        System.out.printf("Hola %s!!!%n", name);


        // ------------------------------------------------------------------------------
        //  EJERCICIO 2
        // Modifica el programa anterior para que además se muestre tu dirección y
        // tu número de teléfono. Asegúrate de que los datos se muestran en líneas
        // separadas y guarda la información en variables.
        // ------------------------------------------------------------------------------

        String address;
        int phoneNum;
        System.out.println("Dime tu nombre: ");
        name = sc.nextLine();

        System.out.println("Dime tu dirección: ");
        address = sc.nextLine();

        System.out.println("Dime tu Número de teléfono: ");
        phoneNum = sc.nextInt();
        sc.nextLine();

        System.out.printf("Nombre: %s%nDirección: %s%nTeléfono: %d%n", name, address, phoneNum);



        // ------------------------------------------------------------------------------
        // EJERCICIO 3
        // Crea la variable nombre y asígnale tu nombre completo. Muestra su valor
        // por pantalla de tal forma que el resultado del programa sea el mismo
        // que en el ejercicio 1.
        // ------------------------------------------------------------------------------

        String surName;

        System.out.println("Dime tu nombre:");
        name = sc.nextLine();
        System.out.println("Dime tus apellidos:");
        surName = sc.nextLine();


        System.out.printf("Hola %s %s!!!%n", name,surName);

        // ------------------------------------------------------------------------------
        //  EJERCICIO 4
        // Crea las variables nombre, direccion y telefono y asígnale los valores
        // correspondientes. Muestra los valores de esas variables por pantalla de
        // tal forma que el resultado del programa sea el mismo que en el ejercicio 2.
        // ------------------------------------------------------------------------------

        // fixme No entiendo, Ya está hecho...

        // ------------------------------------------------------------------------------
        // todo EJERCICIO 5
        // Escribe un programa en el que se declaren las variables enteras x e y.
        // Asígnales los valores 144 y 999 respectivamente. A continuación, muestra
        // por pantalla el valor de cada variable, la suma, la resta, la división
        // y la multiplicación.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 6
        // Realiza un conversor de euros a dólares. La cantidad en euros que se
        // quiere convertir deberá estar almacenada en una variable.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 7
        // Realiza un conversor de dólares a euros. La cantidad en dólares que se
        // quiere convertir deberá estar almacenada en una variable.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 8
        // Escribe un programa que calcule el total de una factura a partir de la
        // base imponible (precio sin IVA). La base imponible estará almacenada
        // en una variable.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 9
        // Crea un programa que use el operador ternario para mostrar el valor
        // absoluto de un número de la siguiente forma:
        // • Si el número es positivo, se mostrará tal cual.
        // • Si es negativo, se mostrará cambiado de signo.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 10
        // Usa el operador ternario para calcular el menor de dos números.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 11
        // Realiza un programa que utilice tres variables enteras: edad, nivel_estudios
        // e ingresos. El programa deberá guardar en una variable booleana resultado:
        // Verdadero → si la edad es menor o igual a 28 y el nivel de estudios es
        // mayor que tres, o bien, la edad es menor de 30 y los ingresos superan
        // los 28000€.
        // Falso → En caso contrario.
        // Utilizar el operador ternario obligatoriamente.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 12
        // Realiza un conversor de euros a dólares. La cantidad de euros que se
        // quiere convertir debe ser introducida por teclado.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 13
        // Realiza un conversor de dólares a euros. La cantidad de dólares que se
        // quiere convertir debe ser introducida por teclado.
        // ------------------------------------------------------------------------------


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 14
        // Realiza un programa que calcule la nota que hace falta sacar en el segundo
        // examen de la asignatura Programación para obtener la media deseada.
        // Hay que tener en cuenta que la nota del primer examen cuenta el 40% y la
        // del segundo examen un 60%.
        //
        // Ejemplo 1:
        // Introduce la nota del primer examen: 7
        // ¿Qué nota quieres sacar en el trimestre? 8.5
        // Para tener un 8.5 en el trimestre necesitas sacar un 9.5 en el segundo examen.
        //
        // Ejemplo 2:
        // Introduce la nota del primer examen: 8
        // ¿Qué nota quieres sacar en el trimestre? 7
        // Para tener un 7 en el trimestre necesitas sacar un 6.33 en el segundo examen.
        // ------------------------------------------------------------------------------


    }
}
