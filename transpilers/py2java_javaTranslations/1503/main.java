public void SUM ( n , m ) {
    if (( var m == 1 )) {
        return ( n * ( n + 1 ) / 2 );
    }
     sum = SUM ( n , m - 1 );
    return int ( sum * ( sum + 1 ) / 2 );
}
n = 5;
m = 3;
System.out.println ( "SUM(" , n , ", " , m , "):" , SUM ( n , m ) );
