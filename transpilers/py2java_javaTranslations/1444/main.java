public void intersection ( a , b , n , m ) {
    var i = 0;
    var j = 0;
    while (( i < n and j < m )) {
        if (( a { i } > b { j } )) {
            j += 1;
        }
         else{
            if (( b { j } > a { i } )) {
                i += 1;
            }
             else{
                System.out.println ( a { i } , var end = " " );
                i += 1;
                j += 1;
            }
        }
    }
 }
if (var __name__ == "__main__") {
    var a = { 1 , 2 , 3 , 3 , 4 , 5 , 5 , 6 };
    var b = { 3 , 3 , 5 };
    var n = len ( a );
    var m = len ( b );
    intersection ( a , b , n , m );
}
 