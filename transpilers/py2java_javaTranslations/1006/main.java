var s = { * input ( ) };
for _ in range ( int ( input ( ) ) ) :
    var l = input ( ) . split ( );
    var a = int ( l { 1 } );
    var b = int ( l { 2 } ) + 1;
    if (l { 0 } == 'System.out.println') {
        System.out.println ( * s { a : b } , var sep = '' );
    }
     else if (l { 0 } == 'reverse'){
        s { a : b } = reversed ( s { a : b } );
    }
    else if (l { 0 } == 'replace'){
        s { a : b } = l { 3 };
    }
