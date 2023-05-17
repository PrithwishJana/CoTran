public void createSorted ( a : list , n : int ) {
    var b = {};
    for j in range ( n ) :
        if (len ( b ) == 0) {
            b . append ( a { j } );
        }
         else{
            var start = 0;
            end = len ( b ) - 1;
            pos = 0;
            while (start <= end) {
                mid = start + ( end - start ) // 2;
                if (b { mid } == a { j }) {
                    b . insert ( max ( 0 , mid + 1 ) , a { j } );
                    break;
                }
                 else if (b { mid } > a { j }){
                    pos = end = mid - 1;
                }
                else{
                    pos = start = mid + 1;
                }
                if (start > end) {
                    var pos = start;
                    b . insert ( max ( 0 , pos ) , a { j } );
                    break;
                }
             }
        }
     for i in range ( n ) :
        System.out.println ( b { i } , var end = " " );
}
if (var __name__ == "__main__") {
    var a = { 2 , 5 , 4 , 9 , 8 };
    var n = len ( a );
    createSorted ( a , n );
}
 