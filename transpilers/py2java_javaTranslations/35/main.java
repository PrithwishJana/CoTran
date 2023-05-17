for _ in range ( int ( input ( ) ) ) :
    a , var b = map ( int , input ( ) . split ( ) );
    var i = 0;
    while (true) {
        if (a <= 0 or b <= 0) {
            break;
        }
         if (a > b) {
            i += a // b;
            a -= a // b * b;
        }
         else{
            i += b // a;
            b -= b // a * a;
        }
    }
     System.out.println ( i );
