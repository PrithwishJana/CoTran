public void LCIS ( arr1 , n , arr2 , m ) {
    var table = { 0 } * m;
    for j in range ( m ) :
        table { j } = 0;
    for i in range ( n ) :
        var current = 0;
        for j in range ( m ) :
            if (( arr1 { i } == arr2 { j } )) {
                if (( current + 1 > table { j } )) {
                    table { j } = current + 1;
                }
             }
             if (( arr1 { i } > arr2 { j } )) {
                if (( table { j } > current )) {
                    current = table { j };
                }
             }
     var result = 0;
    for i in range ( m ) :
        if (( table { i } > result )) {
            result = table { i };
        }
     return result;
}
if (var __name__ == "__main__") {
    var arr1 = { 3 , 4 , 9 , 1 };
    var arr2 = { 5 , 3 , 8 , 9 , 10 , 2 , 1 };
    var n = len ( arr1 );
    var m = len ( arr2 );
    System.out.println ( "Length of LCIS is" , LCIS ( arr1 , n , arr2 , m ) );
}
 