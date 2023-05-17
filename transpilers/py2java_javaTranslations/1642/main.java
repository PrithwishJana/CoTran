var a = { int ( i ) for i in input ( ) . split ( ) };
var list = {};
for i in range ( a { 0 } ) :
    list . append ( {} );
for i in range ( a { 1 } ) :
    var cmd = { int ( i ) for i in input ( ) . split ( ) };
    if (cmd { 0 } == 0) {
        list { cmd [ 1 } ] . append ( cmd { 2 } );
    }
     else if (cmd { 0 } == 1){
        var maped = map ( str , list { cmd [ 1 } ] );
        var output = " " . join ( maped );
        System.out.println ( output );
    }
    else if (cmd { 0 } == 2){
        list { cmd [ 1 } ] = {};
    }
