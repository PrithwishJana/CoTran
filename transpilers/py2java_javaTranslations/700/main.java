var a = {};
for i in range ( 4 ) :
    data = input ( ) . split ( );
    a . append ( { int ( i ) for i in data } );
public void func ( a ) {
    var band = 0;
    for i in range ( 4 ) :
        if (a { i } { 3 } == 1) {
            if (a { ( i + 2 ) % 4 } { 1 }) {
                band = 1;
            }
             if (a { ( i + 1 ) % 4 } { 0 } or a { ( i + 3 ) % 4 } { 2 }) {
                band = 1;
            }
             if (a { i } { 0 } or a { i } { 1 } or a { i } { 2 }) {
                band = 1;
            }
         }
     if (band) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
func ( a );
