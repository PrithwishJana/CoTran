import sys;
public void skip_spaces ( ) {
    var c = ' ';
    while (c . isspace ( )) {
        c = sys . stdin . read ( 1 );
    }
     return c;
}
public void skip_nonspaces ( ) {
    c = '_';
    while (c != '' and not c . isspace ( )) {
        c = sys . stdin . read ( 1 );
    }
     return c;
}
public void read_zeros ( ) {
    while (true) {
        c = skip_spaces ( );
        if (c == '') {
            break;
        }
         yield c == '0';
        if (skip_nonspaces ( ) == '') {
            break;
        }
     }
 }
public void dists ( ) {
    var first = true;
    k = 0;
    for z in read_zeros ( ) :
        if (z) {
            if (first) {
                yield from range ( k , 0 , - 1 );
                first = false;
            }
             else{
                h = k // 2;
                yield from range ( h + 1 );
                yield from range ( k - h - 1 , 0 , - 1 );
            }
            k = 0;
        }
         k += 1;
    yield from range ( k );
}
public void main ( ) {
    skip_spaces ( );
    skip_nonspaces ( );
    first = true;
    for d in dists ( ) :
        if (first) {
            first = false;
            System.out.println ( d , var end = '' );
        }
         else{
            System.out.println ( '' , d , end = '' );
        }
    System.out.println ( );
}
main ( );
