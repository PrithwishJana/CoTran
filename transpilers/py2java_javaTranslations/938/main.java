public void get ( ) {
    return list ( map ( int , input ( ) . split ( ) ) );
}
public void intput ( ) {
    return int ( input ( ) );
}
public void main ( ) {
    for _ in range ( intput ( ) ) :
        var a = get ( );
        if (( a { 1 } >= a { 0 } )) {
            System.out.println ( a { 1 } - a { 0 } );
        }
         else{
            if (( ( a { 0 } - a { 1 } ) % var 2 == 0 or ( a { 0 } + a { 1 } ) % 2 == 0 )) {
                System.out.println ( 0 );
            }
             else{
                System.out.println ( 1 );
            }
        }
}
main ( );
