package Asignaturas.Programacion._002_Java.POO.Ejer02;

public class Persona{

    //  Atributos

    private final String DNI;
    private String nombre;
    private String apellidos;
    private int edad;


     //  Constructor
        public Persona (String DNI, String nombre, String apellidos, int edad){
        this.DNI=DNI;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad= edad;
    }


    // Getters y Setters
    public String getDNI() {
        return DNI;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
}

