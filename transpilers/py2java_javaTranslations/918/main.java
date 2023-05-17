var t = int ( input ( ) );
while (t > 0) {
    t -= 1;
    n , l , var r = map ( int , input ( ) . split ( ) );
    var k = n // l;
    if (r * k >= n) {
        System.out.println ( 'Yes' );
    }
     else{
        System.out.println ( 'No' );
    }
}
 