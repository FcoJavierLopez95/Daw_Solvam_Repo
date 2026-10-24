package _0001_Ejercicios_Java_21_10_2026;
import java.util.Scanner;

public class _0001_Ejercicios_Java_21_10_2026 {
    public static void main(String[] args) {
        // ------------------------------------------------------------------------------
        // todo EJERCICIO 1
        // Escribe un programa que pida por teclado un día de la semana y que diga
        // qué asignatura toca a primera hora ese día.
        // ------------------------------------------------------------------------------
        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 1");
        System.out.println();


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
            } catch (Exception e) {
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
        // EJERCICIO 2
        // Realiza un programa que pida una hora por teclado y que muestre luego
        // buenos días, buenas tardes o buenas noches según la hora. Se utilizarán
        // los tramos de 6 a 12, de 13 a 20 y de 21 a 5 respectivamente. Sólo se tienen
        // en cuenta las horas, los minutos no se deben introducir por teclado.
        // ------------------------------------------------------------------------------

        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 2");
        System.out.println();


        int hora = -1;
        String saludo = "";
        do{
            System.out.println("Dime que hora es: Solo la hora de 00 a 23");
            try {
                hora = sc.nextInt();

                if (hora >= 6 && hora <= 12){
                    saludo = "Buenos días";
                }else if(hora >= 13 && hora <= 20){
                    saludo = "Buenas tardes";
                }else  if((hora >= 21 && hora <= 23) || (hora >= 0 && hora <= 5)){
                   saludo = "Buenas noches";
                }else{
                    System.out.println("El número tiene que estar entre 0 y 23");
                }
            } catch (Exception e) {
                System.out.println("El valor que has introducido no es un número, inténtalo de nuevo.");
                }
            sc.nextLine();

        }while (hora < 0 || hora > 23);

        System.out.println(saludo);

        // ------------------------------------------------------------------------------
        // EJERCICIO 3
        // Calcula la nota de un trimestre de la asignatura Programación. El programa
        // pedirá las dos notas que ha sacado el alumno en los dos primeros controles.
        // Si la media de los dos controles da un número mayor o igual a 5, el alumno
        // está aprobado y se mostrará la media. En caso de que la media sea un número
        // menor que 5, el alumno habrá tenido que hacer el examen de recuperación que
        // se califica como apto o no apto, por tanto se debe preguntar al usuario
        // ¿Cuál ha sido el resultado de la recuperación? (apto/no apto). Si el resultado
        // de la recuperación es apto, la nota será un 5; en caso contrario, se mantiene
        // la nota media anterior.

        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 3");
        System.out.println();

        // Declaración de variables
        int examenes = 0;
        float nota;
        float notatotal=0f;
        int recuperacion;

        // Pregunto cuantos examenes han hecho este trimestre.
        do {
            System.out.println("Cuantos exámenes has hecho este trimestre?");

            try {
                examenes = sc.nextInt();
            } catch (Exception e) {
                System.out.println("Has introducido un valor no válido. Por favor inténtalo de nuevo:");
                }
            sc.nextLine();

            if (examenes <0) {
                System.out.println("El número no puede ser negativo");
            }
        }while(examenes <=0);

        // Pido las notas de los exámenes
        for (int i = 1; i < examenes+1; i++) {

            do {
                try {
                    System.out.printf("Dime la nota del examen %d%n", i);
                    nota = sc.nextFloat();

                    if (nota <= 0 || nota > 10) {
                    System.out.println("La nota no puede ser negativa ni mayor a 10");
                    }

                } catch (Exception e) {
                    System.out.println("El valor introducido no es un numero, inténtalo de nuevo");
                    nota = -1f;
                    sc.nextLine();
                    }
            } while (nota <= 0 || nota > 10);
            notatotal = notatotal + nota;
        }

            // Calculo la media y si tiene que recuperar
        float media = notatotal / examenes;
        System.out.printf("Tu nota final es un %f", media);

            if (media >= 5) {
                System.out.printf("La media de Programación es de %f%n", media);
            } else {
                System.out.println("Tienes que hacer recuperación");
                do {
                    System.out.printf("Que has sacado?%n1.-Apto%n2.-No apto%n");
                    System.out.printf("Que has sacado?%n1.-Apto%n2.-No apto%n");
                    try {
                        recuperacion = sc.nextInt();
                        if(recuperacion == 1){
                            media = 5f;
                        }
                        else if (recuperacion== 2) {
                            System.out.println("Que pena no has aprobado");
                        }
                        else{
                            System.out.println("Solo puedes introducir 1  y 2");
                        }
                    } catch(Exception e){
                        System.out.println("Has introducido un valor no válido. Por favor inténtalo de nuevo:");
                        recuperacion = 0;
                        }
                    sc.nextLine();

                }while (recuperacion != 1 && recuperacion !=2);

            }
        System.out.printf("Tu nota final en Programación es %f", media);


        // ------------------------------------------------------------------------------
        // EJERCICIO 4
        // Muestra los números múltiplos de 5 de 0 a 100 utilizando un bucle for,
        // un bucle while y un bucle do-while.
        // ------------------------------------------------------------------------------

        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 4");
        System.out.println();


        for (int i=0; i <= 100; i++){
            if (i % 5 == 0 && i != 0){
                System.out.printf("%d es múltiplo de 5%n", i);
            }
            else{
                System.out.println(i);
            }
        }


        // ------------------------------------------------------------------------------
        // EJERCICIO 5
        // Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás
        // utilizando un bucle for, un bucle while y un bucle do-while.
        // ------------------------------------------------------------------------------
        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 5");
        System.out.println();


        for (int i = 360; i > 160; i-=20) {
            System.out.println(i);
        }


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


        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 6");
        System.out.println();

        // Declaración de variables
        final float GEN = 1.21f;
        final float RED = 1.10f;
        final float SUPRED = 1.04f;
        float NOPRO = 1f;
        float MITAD = 0.5f;
        float FIVEPOR = 0.05f;
        float MNFIVE = -5f;


        float bImp = 0f;
        float iva = 0f;
        float desc = 0f;
        float price = -1f;


        // Pregunto Base imp.

        do {
            System.out.println("Introduce el precio del artículo");
            bImp = 0f;

            try {
                bImp = sc.nextFloat();
            } catch (Exception e) {
                System.out.println("Has introducido un valor no válido. Por favor inténtalo de nuevo:");
            }
            sc.nextLine();

            if (bImp <=0) {
                System.out.println("El número no puede ser 0 ni negativo");
            }
        }while(bImp <=0);

        // pregunto tipo IVA.
        menu = 0;

        do{
            System.out.printf("Dime a que tipo de base imponible esta sujeto:%n·1.-General: 21%%%n·2.-Reducido: 10%%%n·3-.Super reducido: 4%%%n");

            try {
                menu = sc.nextInt();

                switch (menu) {
                    case (1):
                        iva = GEN;
                        break;
                    case (2):
                        iva = RED;
                        break;
                    case (3):
                        iva = SUPRED;
                        break;
                    default:
                        System.out.println("El valor tiene que ser 1, 2 o 3");
                        menu = 0;
                        break;
                }

            } catch (Exception e) {
                System.out.println("El dato introducido no es válido, por favor inténtalo de nuevo");
                menu = 0;
            }sc.nextLine();
        }while (menu == 0);


        // Código de descuento
        String desCode = "";
        do {
            System.out.println("Introduce tu código de descuento(nopro, mitad, meno5 o 5porc)");
            desCode = sc.nextLine();

            switch (desCode) {
                case ("nopro"):
                    desc = NOPRO;
                    break;
                case ("mitad"):
                    desc = MITAD;
                    break;
                case ("5porc"):
                    desc = FIVEPOR;
                    break;
                case ("meno5"):
                    desc = MNFIVE;
                    break;
                default:
                    System.out.println("Fas introduciro un valor no válido, inténtalo de nuevo");
                    desCode = "";

            }
        }while(desCode.equals(""));
        float descPrint=0f;
        // total
        if (desc <0) {
            price = (bImp * iva) + desc;
            descPrint = desc;
        }else{
            price = bImp * iva * desc;
            descPrint = (desc * 100);
        }

        // Conclusión:
        float ivaPrint = (iva -1) *100;
        System.out.printf("Base Imponible; %f %n IVA %f%% %n Descuento %f %n precio final: %f%n", bImp, ivaPrint, descPrint,  price);


        // ------------------------------------------------------------------------------
        // todo EJERCICIO 7
        // Realiza el control de acceso a una caja fuerte. La combinación será un número
        // de 4 cifras. El programa nos pedirá la combinación para abrirla. Si no
        // acertamos, se nos mostrará el mensaje “Lo siento, esa no es la combinación”.
        // Si acertamos se nos dirá “La caja fuerte se ha abierto satisfactoriamente”.
        // Tendremos cuatro oportunidades para abrir la caja fuerte.
        // ------------------------------------------------------------------------------

        System.out.printf("%n%n");
        System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
        System.out.println("Ejercicio 7");
        System.out.println();




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