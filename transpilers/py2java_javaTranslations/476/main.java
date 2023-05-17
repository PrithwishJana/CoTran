import math.sqrt;
public void find_Area ( a ) {
    var R = a * ( 2.0 - sqrt ( 2 ) ) ;;
    var area = 3.14 * R * R / 2.0 ;;
    return area ;;
}
if (var __name__ == "__main__") {
    var a = 4 ;;
    System.out.println ( "Area of var semicircle =" , "{:.4f}" . format ( find_Area ( a ) ) ) ;;
}
 