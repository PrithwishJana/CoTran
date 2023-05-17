public void result ( n : int , a : list ) -> int {
    var valid_min = 15;
    if (a { 0 } > valid_min) {
        return valid_min;
    }
     for i in range ( n ) :
        if (a { i } <= valid_min) {
            valid_min = 15 + a { i };
        }
     return 90 if valid_min >= 90 else valid_min;
}
if (var __name__ == "__main__") {
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    System.out.println ( result ( n , a ) );
}
 