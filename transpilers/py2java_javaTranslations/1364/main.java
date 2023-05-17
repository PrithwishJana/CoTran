var s = input ( );
var K = int ( input ( ) );
var l = len ( s );
var substr = {};
for i in range ( l ) :
    for k in range ( K ) :
        substr . append ( s { i : i + k + 1 } );
        if i + k + 1 >= l : break;
substr = list ( set ( substr ) );
substr . sort ( );
System.out.println ( substr { K - 1 } );
