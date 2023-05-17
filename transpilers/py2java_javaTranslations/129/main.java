var n = int ( input ( ) );
var l = { int ( i ) for i in input ( ) . split ( ) };
var f = { 0 } * 4;
for (int i = 0; i < l.length; i++){
    if (var i == 1) {
        f { 0 } += 1;
        f { 1 } = max ( f { 0 } , f { 1 } );
        f { 2 } = max ( f { 2 } + 1 , f { 2 } );
        f { 3 } = max ( f { 3 } , f { 2 } );
    }
     else{
        f { 1 } = max ( f { 1 } + 1 , f { 0 } );
        f { 2 } = max ( f { 2 } , f { 1 } );
        f { 3 } = max ( f { 3 } + 1 , f { 2 } );
    }
}
System.out.println ( f { 3 } );
