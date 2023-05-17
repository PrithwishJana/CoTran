public void test ( ) {
    nrow , var ncol = map ( int , input ( ) . split ( ) );
    var arr = {};
    var val = 100000000000;
    lr , lc = 0 , 0;
    for row_id in range ( nrow ) :
        temp = list ( input ( ) );
        arr . append ( {} );
        for col_id in range ( ncol ) :
            if (temp { col_id } == "R") {
                temp2 = row_id + col_id;
                arr { row_id } . append ( temp2 );
                if (temp2 < val) {
                    val = temp2;
                    lr , lc = row_id , col_id;
                }
             }
             else{
                arr { row_id } . append ( 0 );
            }
    for i in range ( lr ) :
        temp = arr { i };
        if (max ( temp ) > 0) {
            return false;
        }
     for i in range ( nrow ) :
        for j in range ( lc ) :
            if (arr { i } { j } > 0) {
                return false;
            }
     return true;
}
num_test_cases = int ( input ( ) );
for test_case in range ( num_test_cases ) :
    val = test ( );
    if (val) {
        System.out.println ( 'YES' );
    }
     else{
        System.out.println ( 'NO' );
    }
