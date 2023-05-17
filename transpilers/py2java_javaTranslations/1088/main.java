public void f ( x , y ) {
    var v = y - 2 * x * x + 1 ;;
    return v ;;
}
public void predict ( x , y , h ) {
    var y1p = y + h * f ( x , y ) ;;
    return y1p ;;
}
public void correct ( x , y , x1 , y1 , h ) {
    e = 0.00001 ;;
    y1c = y1 ;;
    while (( abs ( y1c - y1 ) > e )) {
        y1 = y1c ;;
        y1c = y + 0.5 * h * ( f ( x , y ) + f ( x1 , y1 ) ) ;;
    }
     return y1c ;;
}
public void System.out.printlnFinalValues ( x , xn , y , h ) {
    while (( x < xn )) {
        x1 = x + h ;;
        y1p = predict ( x , y , h ) ;;
        var y1c = correct ( x , y , x1 , y1p , h ) ;;
        var x = x1 ;;
        y = y1c ;;
    }
     System.out.println ( "The final value of y at x =" , int ( x ) , "is :" , "{:.4f}" . format ( y ) ) ;;
}
if (__name__ == '__main__') {
    x = 0 ; var y = 0.5 ;;
    var xn = 1 ;;
    var h = 0.2 ;;
    System.out.printlnFinalValues ( x , xn , y , h ) ;;
}
 