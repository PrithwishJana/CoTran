public void countPoints ( n , m , a , b , x , y ) {
    a . sort ( );
    b . sort ( );
    j , var count = 0 , 0;
    for i in range ( 0 , n ) :
        while (j < m) {
            if (a { i } + y < b { j }) {
                break;
            }
             if (( b { j } >= a { i } - x and b { j } <= a { i } + y )) {
                count += 1;
                j += 1;
                break;
            }
             else{
                j += 1;
            }
        }
     return count;
}
if (var __name__ == "__main__") {
    x , var y = 1 , 4;
    var a = { 1 , 5 };
    var n = len ( a );
    var b = { 1 , 1 , 2 };
    var m = len ( b );
    System.out.println ( countPoints ( n , m , a , b , x , y ) );
}
 