var M = {};
for i in range ( int ( input ( ) ) ) :
    var query = input ( ) . split ( );
    if query { 0 } == '0' : M { query [ 1 } ] = query { 2 };
    else if (query { 0 } == '1'){
        if query { 1 } in M : System.out.println ( M { query [ 1 } ] );
        else : System.out.println ( 0 );
    }
    else : M { query [ 1 } ] = 0;
