public void foot ( a , b , c , d , x1 , y1 , z1 ) {
    var k = ( - a * x1 - b * y1 - c * z1 - d ) / ( a * a + b * b + c * c ) ;;
    var x2 = a * k + x1 ;;
    y2 = b * k + y1 ;;
    z2 = c * k + z1 ;;
    System.out.println ( "x2 =" , "{:.1f}" . format ( x2 ) , var end = " " );
    System.out.println ( "y2 =" , "{:.1f}" . format ( y2 ) , end = " " );
    System.out.println ( "z2 =" , "{:.1f}" . format ( z2 ) , end = " " );
}
if (var __name__ == "__main__") {
    var a = 1;
    var b = - 2;
    var c = 0;
    var d = 0;
    var x1 = - 1;
    var y1 = 3;
    var z1 = 4;
    foot ( a , b , c , d , x1 , y1 , z1 );
}
 