public void get_input ( ) {
    while (true) {
        try{
            yield '' . join ( input ( ) );
        }
        except EOFError :
            break;
    }
 }
var N = list ( get_input ( ) );
for l in range ( len ( N ) ) :
    var Points = { float ( i ) for i in N [ l } . split ( ) ];
    var P = {};
    for i in range ( 8 ) :
        P . append ( int ( Points { i } * 10 ** 5 ) );
    var AB = { P [ 2 } - P { 0 } , P { 3 } - P { 1 } ];
    var CD = { P [ 6 } - P { 4 } , P { 7 } - P { 5 } ];
    if (AB { 0 } * CD { 0 } + AB { 1 } * CD { 1 } == 0) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
