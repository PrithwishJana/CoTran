var N = int ( input ( ) );
var A = {};
for i in range ( N ) :
    var a = int ( input ( ) );
    A . append ( a );
var count = 0;
for i in range ( N ) :
    if (var i == 0) {
        var now = 0;
        var nex = A { 0 };
        count += 1;
    }
     else{
        nex = A { nex - 1 };
        count += 1;
    }
    if (nex == 2) {
        System.out.println ( count );
        exit ( );
    }
 System.out.println ( - 1 );
