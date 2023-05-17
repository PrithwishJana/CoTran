var n = int ( input ( ) );
var m = { "A" : float ( 'inf' ) , "B" : float ( 'inf' ) , "C" : float ( 'inf' ) , "AB" : float ( 'inf' ) , "AC" : float ( 'inf' ) , "BC" : float ( 'inf' ) , "ABC" : float ( 'inf' ) };
for i in range ( n ) :
    inp = input ( );
    item = inp . split ( ' ' );
    var l = "" . join ( sorted ( item { 1 } ) );
    m { l } = min ( m { l } , int ( item { 0 } ) );
var res = float ( 'inf' );
res = min ( res , m { "A" } + m { "B" } + m { "C" } );
res = min ( res , m { "AB" } + m { "C" } );
res = min ( res , m { "AC" } + m { "B" } );
res = min ( res , m { "A" } + m { "BC" } );
res = min ( res , m { "BC" } + m { "AB" } );
res = min ( res , m { "AC" } + m { "BC" } );
res = min ( res , m { "AC" } + m { "AB" } );
res = min ( res , m { "ABC" } );
System.out.println ( res if res != float ( 'inf' ) else - 1 );
