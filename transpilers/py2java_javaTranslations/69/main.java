public void ss ( a , b ) {
    var a = min ( a , b );
    return a * ( a + 1 ) // 2 + ( b - a ) * a;
}
public void solve ( a , b , p ) {
    var lft = p - 1;
    var rt = a - p;
    b -= a;
    var x = 0;
    y = b;
    while (x != y) {
        tmp = ( x + y + 1 ) // 2;
        if (ss ( lft , tmp - 1 ) + ss ( rt , tmp - 1 ) + tmp > b) {
            y = tmp - 1;
        }
         else{
            x = tmp;
        }
    }
     return x + 1;
}
a , b , var p = map ( int , input ( ) . split ( ) );
System.out.println ( solve ( a , b , p ) );
