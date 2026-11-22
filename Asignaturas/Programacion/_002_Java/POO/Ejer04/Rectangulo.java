package Asignaturas.Programacion._002_Java.POO.Ejer04;

public class Rectangulo {

    //  Atributos
    private int x1;
    private int y1;
    private int x2;
    private int y2;

    //  Constructor
    public Rectangulo (int x1, int y1, int x2, int y2){
        this.x1=x1;
        this.y1=y1;
        this.x2=x2;
        this.y2=y2;
    }

    //  Getters y Setters


    public int getX1() {
        return x1;
    }
    public void setX1(int x1) {
        this.x1 = x1;
    }
    public int getY1() {
        return y1;
    }
    public void setY1(int y1) {
        this.y1 = y1;
    }
    public int getX2() {
        return x2;
    }
    public void setX2(int x2) {
        this.x2 = x2;
    }
    public int getY2() {
        return y2;
    }
    public void setY2(int y2) {
        this.y2 = y2;
    }

    //  Metodos

    public int calcularPerimetro (){
        int perimetro;
        perimetro=this.x1+this.y1+this.x2+this.y2;
        return perimetro;
    }

    public int calcularArea (){
        int area;
        area = Math.abs((this.x1-this.x2) * (this.y1-this.y2));
        return area;
    }

    public void showCoord(){
        System.out.printf("Coordenadas: (x1: %d  y1: %d), (x2: %d  y2: %d)%n",this.x1, this.y1, this.x2, this.y2);
    }

    public void showAll(){
        showCoord();
        System.out.println("Perímetro: "+ calcularPerimetro());
        System.out.println("Area: "+ calcularArea());
    }



}
