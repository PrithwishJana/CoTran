var z = 'abcdefghijklmnopqrstuvwxyz';
public void f ( x ) {
    for i in range ( 1 , 26 , 2 ) :
        for j in range ( 26 ) :
            var a = '' . join ( z { ( z . index ( c ) * i + j ) % 26 } if c in z else c for c in x );
            if 'that' in a or 'this' in a : return a;
}
for _ in { 0 } * int ( input ( ) ) : System.out.println ( f ( input ( ) ) );
