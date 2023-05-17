import sys;
public void makeEven ( arr , n ) {
    var first_e_i = - 1;
    last_e_i = - 1;
    last_n_i = n - 1;
    for i in range ( n ) :
        if (( int ( arr { i } ) % 2 == 0 and int ( arr { i } ) < int ( arr { last_n_i } ) )) {
            first_e_i = i;
            break;
        }
         if (int ( arr { i } ) % 2 == 0) {
            last_e_i = i;
        }
     if (first_e_i != - 1) {
        ( arr { first_e_i } , arr { last_n_i } ) = ( arr { last_n_i } , arr { first_e_i } );
        return arr;
    }
     if (first_e_i == - 1 and last_e_i != - 1) {
        ( arr { last_e_i } , arr { last_n_i } ) = ( arr { last_n_i } , arr { last_e_i } );
        return arr;
    }
     return arr;
}
if (var __name__ == '__main__') {
    var string = "1356425";
    var result = "" . join ( makeEven ( list ( string ) , len ( list ( string ) ) ) );
    System.out.println ( result );
}
 