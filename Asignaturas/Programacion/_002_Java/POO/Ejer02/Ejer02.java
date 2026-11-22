package Asignaturas.Programacion._002_Java.POO.Ejer02;

import java.util.Scanner;
public class Ejer02{

    public static void main(String[] args) {

        Persona Spiderman = new  Persona( "43545456J", "Peter", "Parker",27);
        Persona Ironman = new Persona("34563467I", "Tonny", "Stark", 43);

        Persona p1 = pedirDatos();
        Persona p2 = pedirDatos();

        comprobarMayoriaEdad(p1);
        comprobarMayoriaTernario(p2);
        comprobarMayoriaEdad(Spiderman);
        comprobarMayoriaTernario(Ironman);


    }   //  Cierre del Main

    public static Persona pedirDatos(){
    Scanner Scanner = new Scanner(System.in);
        System.out.println("Dine tu DNI:");
    final String DNI = Scanner.nextLine();
        System.out.println("Dine tu Nombre:");
    String nombre = Scanner.nextLine();
        System.out.println("Dine tus Apellidos:");
    String apellidos = Scanner.nextLine();
        System.out.println("Dine tu Edad:");
    int edad = Scanner.nextInt();
        Scanner.nextLine();
        System.out.println("Persona  Creada satisfactoriamente.");
    return  new Persona (DNI, nombre, apellidos, edad);
    }
    public static void comprobarMayoriaEdad(Persona p) {
        String condicion;
        if (p.getEdad() >= 18) {
            condicion = " es mayor de edad";
        } else {
            condicion = " no es mayor de edad";
        }
        System.out.printf("%s %s con DNI:%s %s %n", p.getNombre(), p.getApellidos(), p.getDNI(), condicion);
    }

        //Solución con ternarios
        public static void comprobarMayoriaTernario(Persona p) {
        String condicion = p.getEdad() >= 18 ? " es Mayor de Edad" : " no es mayor de Edad";
        System.out.printf("%s %s con DNI:%s %s%n",p.getNombre(), p.getApellidos(), p.getDNI(), condicion);
    }




}

