x , var y = map ( int , input ( ) . split ( ) );
var CielWon = false;
while (( y > 1 and x * 10 + y > 21 )) {
    t = min ( x , 2 );
    x -= t;
    y -= ( 2 - t ) * 10 + 2;
    if (( y < 2 or 10 * x + y < 22 )) {
        CielWon = true;
        break;
    }
     y -= 2;
    var t = min ( 2 , y // 10 );
    y -= 10 * t;
    x -= 2 - t;
}
 System.out.println ( 'Ciel' if CielWon else 'Hanako' );
