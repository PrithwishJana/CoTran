var h = int ( input ( ) );
for x in range ( h ) :
    a , b = map ( int , input ( ) . split ( ) );
    n , m = map ( int , input ( ) . split ( ) );
    s = min ( m , b );
    m -= s;
    b -= s;
    while (a % 10 == 0) {
        b += 1;
        a = a // 10;
    }
     while (n % 10 == 0) {
        m += 1;
        n = n // 10;
    }
     h = str ( a );
    var k = str ( n );
    if (len ( h ) + b > len ( k ) + m) {
        System.out.println ( '>' );
    }
     else if (len ( h ) + b < len ( k ) + m){
        System.out.println ( '<' );
    }
    else{
        if (h > k) {
            System.out.println ( '>' );
        }
         else if (h < k){
            System.out.println ( '<' );
        }
        else{
            System.out.println ( '=' );
        }
    }
