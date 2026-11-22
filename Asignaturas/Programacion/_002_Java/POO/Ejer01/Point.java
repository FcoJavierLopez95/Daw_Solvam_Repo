package Asignaturas.Programacion._002_Java.POO.Ejer01;

// Clase
public class Point {
   private  int x;
    private int y;


    //Constructor

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }


    //  Metodos

    public void showPoint(){
        System.out.printf("Los puntos son: %d %d%n",x ,y);
    }
    public void showCord(){
        System.out.printf("Las coordenadas son: (X=%d Y=%d)%n",x ,y);
    }

    public void desplaza(int dx, int dy){
    x +=dx;
    y +=dy;
    }

  /*  public int distance (int obj, int puntoP){

    }*/



/*
    * - public void setXY(int x, int y): Modifica ambas coordenadas.
    * - public void desplaza(int dx, int dy): Desplaza el punto la cantidad (dx,dy) indicada. Ejemplo: Si (1,1) se desplaza (2,5) estará en (3,6).
    * - public int distancia(Punto p): Calcula y devuelve la distancia entre el propio objeto (this) y otro objeto (Punto p) pasado como parámetro.
*/

    //  Getters y Setters


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void setXY(int x, int  y){
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
}
