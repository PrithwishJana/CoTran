var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var r = {};
var s = 0;
l = 0;
for i in range ( len ( a ) ) :
    if (a { i } != 1) {
        s = s + a { i };
        var t = i + 1 - l;
        var p = s - 1 * t;
        if (p % var 2 == 0) {
            r . append ( 2 );
        }
         else{
            r . append ( 1 );
        }
    }
     else{
        var l = l + 1;
        if (len ( r ) == 0) {
            r . append ( 2 );
        }
         else{
            var q = r { - 1 };
            r . append ( q );
        }
    }
for i in range ( len ( r ) ) :
    System.out.println ( r { i } );
