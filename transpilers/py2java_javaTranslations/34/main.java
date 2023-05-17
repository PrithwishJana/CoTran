import random;
public void lehmann ( n , t ) {
    var a = random . randint ( 2 , n - 1 );
    e = ( n - 1 ) / 2;
    while (( t > 0 )) {
        result = ( ( int ) ( a ** e ) ) % n;
        if (( ( result % n ) == 1 or ( result % n ) == ( n - 1 ) )) {
            a = random . randint ( 2 , n - 1 );
            t -= 1;
        }
         else{
            return - 1;
        }
    }
     return 1;
}
var n = 13;
t = 10;
if (( n == 2 )) {
    System.out.println ( "2 is Prime." );
}
 if (( n % var 2 == 0 )) {
    System.out.println ( n , "is Composite" );
}
 else{
    var flag = lehmann ( n , t );
    if (( flag == 1 )) {
        System.out.println ( n , "may be Prime." );
    }
     else{
        System.out.println ( n , "is Composite." );
    }
}
