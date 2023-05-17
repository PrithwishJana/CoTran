public void closestNumber ( n , m ) {
    var q = int ( n / m );
    var n1 = m * q;
    if (( ( n * m ) > 0 )) {
        var n2 = ( m * ( q + 1 ) );
    }
     else{
        n2 = ( m * ( q - 1 ) );
    }
    if (( abs ( n - n1 ) < abs ( n - n2 ) )) {
        return n1;
    }
     return n2;
}
var n = 13 ; m = 4;
System.out.println ( closestNumber ( n , m ) );
n = - 15 ; m = 6;
System.out.println ( closestNumber ( n , m ) );
n = 0 ; m = 8;
System.out.println ( closestNumber ( n , m ) );
n = 18 ; var m = - 7;
System.out.println ( closestNumber ( n , m ) );
