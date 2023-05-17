import collections.defaultdict;
while (true) {
    var n = int ( input ( ) );
    if (not n) {
        break;
    }
     stars = defaultdict ( int );
    for s in map ( int , input ( ) . split ( ) ) :
        stars { s } += 1;
    half_n = n // 2;
    for i , s in stars . items ( ) :
        if (s > half_n) {
            System.out.println ( i );
            break;
        }
     else{
        System.out.println ( 'NO COLOR' );
    }
}
 