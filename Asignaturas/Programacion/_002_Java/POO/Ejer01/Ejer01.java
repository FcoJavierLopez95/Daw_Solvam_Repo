package Asignaturas.Programacion._002_Java.POO.Ejer01;

public class Ejer01 {

    public static void main(String[] args) {



    /*
     * ============================================================================================================================================
     * todo 1. Ejercicio Punto
     * ============================================================================================================================================
     * fixme APARTADO A – CLASES SIMPLES CON ATRIBUTOS
     * Crea un programa con una clase llamada Punto que representará un punto de dos dimensiones en un plano. Solo contendrá dos atributos
     * enteros llamados x e y (coordenadas). En el main de la clase principal instancia 3 objetos Punto con las coordenadas (5,0), (10,10) y (-3,7).
     *  Muestra por pantalla sus coordenadas (utiliza un println para cada punto). Modifica todas las coordenadas (prueba distintos operadores
     * como = + - += *= ...) y vuelve a imprimirlas por pantalla.
    */

        Point obj1 = new Point(5,0);
        Point obj2 = new Point(10,10);
        Point obj3 = new Point(-3,7);

        obj1.showPoint();
        obj2.showPoint();
        obj3.showPoint();
        System.out.println();

    /*
    --------------------------------------------------------------------------------------------------------------------------------------------
    * fixme APARTADO B – CONSTRUCTORES
    * Modifica el programa del apartado anterior y realiza los cambios indicados. Añade a la clase Punto un constructor con parámetros que copie
    * las coordenadas pasadas como argumento a los atributos del objeto. Corrige el main y utiliza el constructor con parámetros para instanciar
    * los objetos, pasándole como argumento los valores deseados.

         Public
        obj1.x = obj1.x*2;
        obj1.y = obj1.y+2;
        obj2.x = obj2.x/2;
        obj2.y = obj2.y%2;
        obj3.x--;
        obj3.y +=2;

        obj1.showCord();
        obj2.showCord();
        obj3.showCord();
        System.out.println();

    * --------------------------------------------------------------------------------------------------------------------------------------------
    * todo APARTADO C – GETTERS Y SETTERS
    * Modifica el programa del apartado anterior y realiza los cambios indicados. Modifica los atributos de Punto para que sean private. Fíjate
    * que desde el main ya no te dejará utilizar ni modificar los atributos x e y de los objetos. Vamos a añadir los getters: int getX() e
    * int getY() que devolverán los valores de x e y respectivamente. Es una forma indirecta de leer sus valores. Añadiremos también los setters:
    * void setX(int x) y void setY(int y) que copiarán el valor pasado como parámetro a los atributos de la clase. Tanto getters como setters
    * deben ser public. Corrige el main para utilizar los getters y setters. Prueba a instanciar varios objetos, mostrar sus valores, modificarlos, etc.
    */
        Point obj4 = new Point (0,0);
        obj4.setX(100);
        obj4.setY(400);

        obj4.showPoint();
        System.out.println(obj4.getX());
        System.out.println(obj4.getY());


    /*     * --------------------------------------------------------------------------------------------------------------------------------------------
     * fixme APARTADO D – AÑADIENDO MÉTODOS ÚTILES
     * Modifica el programa del apartado anterior y añade los métodos que se indican. Añade a la clase Punto los siguientes métodos públicos:
     * - public void imprime(): Imprime por pantalla las coordenadas. Ejemplo: "(7,-5)"
     * - public void setXY(int x, int y): Modifica ambas coordenadas.
     * - public void desplaza(int dx, int dy): Desplaza el punto la cantidad (dx,dy) indicada. Ejemplo: Si (1,1) se desplaza (2,5) estará en (3,6).
     * - public int distancia(Punto p): Calcula y devuelve la distancia entre el propio objeto (this) y otro objeto (Punto p) pasado como parámetro.
     * Prueba a utilizar estos métodos desde el main para comprobar su funcionamiento.
     */


        obj1.showCord();
        obj2.showCord();
        obj3.showCord();
        obj4.showCord();


    }
}