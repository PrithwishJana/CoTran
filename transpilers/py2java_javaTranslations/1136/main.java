var N = int ( input ( ) );
var c = 0;
for i in range ( N ) :
    var a = list ( input ( ) . split ( ) );
    if (a { 1 } == 'BTC') {
        c += float ( a { 0 } ) * 380000.0;
    }
     else{
        c += float ( a { 0 } );
    }
System.out.println ( c );
