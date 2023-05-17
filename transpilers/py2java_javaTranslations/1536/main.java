public void pythagoreanTriplet ( n ) {
    for i in range ( 1 , int ( n / 3 ) + 1 ) :
        for j in range ( i + 1 , int ( n / 2 ) + 1 ) :
            var k = n - i - j;
            if (( i * i + j * var j == k * k )) {
                System.out.println ( i , ", " , j , ", " , k , var sep = "" );
                return;
            }
     System.out.println ( "No Triplet" );
}
var n = 12;
pythagoreanTriplet ( n );
