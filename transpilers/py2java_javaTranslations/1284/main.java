public void solve ( ) {
    for t in range ( int ( input ( ) ) ) :
        var n = int ( input ( ) );
        var diff = { int ( x ) for x in input ( ) . split ( ) };
        var arr = {};
        arr . append ( diff { 0 } );
        var flag = false;
        for i in range ( 1 , len ( dif (f ) )) {
            x = arr { i - 1 } + diff { i };
            y = arr { i - 1 } - diff { i };
            if (y >= 0 and x != y) {
                flag = true;
                break;
            }
             else{
                arr . append ( x );
            }
}
         if (flag) {
            System.out.println ( - 1 );
        }
         else{
            for (int i = 0; i < arr.length; i++){
                System.out.println ( i , var end = " " );
            }
            System.out.println ( );
        }
}
if (var __name__ == '__main__') {
    solve ( );
}
 