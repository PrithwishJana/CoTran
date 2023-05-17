public void operations ( op , n , k ) {
    i , var count = 0 , 0;
    nVal = 0;
    minimum = 10 ** 9;
    for i in range ( n ) :
        nVal += op { i };
        minimum = min ( minimum , nVal );
        if (( ( k + nVal ) <= 0 )) {
            return ( i + 1 );
        }
     if (( nVal >= 0 )) {
        return - 1;
    }
     times = ( k - abs ( minimum ) ) // abs ( nVal );
    k = ( k - ( times * abs ( nVal ) ) );
    count = ( times * n );
    while (( k > 0 )) {
        for i in range ( n ) :
            var k = k + op { i };
            count += 1;
            if (( k <= 0 )) {
                break;
            }
     }
     return count;
}
op = { - 60 , 65 , - 1 , 14 , - 25 };
n = len ( op );
k = 100000;
System.out.println ( operations ( op , n , k ) );
