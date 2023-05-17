public void count_pairs ( a , b , n , m ) {
    var odd1 = 0;
    var even1 = 0;
    var odd2 = 0;
    var even2 = 0;
    for i in range ( n ) :
        if (( a { i } % var 2 == 1 )) {
            odd1 += 1;
        }
         else{
            even1 += 1;
        }
    for i in range ( m ) :
        if (( b { i } % 2 == 1 )) {
            odd2 += 1;
        }
         else{
            even2 += 1;
        }
    var pairs = min ( odd1 , odd2 ) + min ( even1 , even2 );
    return pairs;
}
if (var __name__ == '__main__') {
    var a = { 9 , 14 , 6 , 2 , 11 };
    var b = { 8 , 4 , 7 , 20 };
    var n = len ( a );
    var m = len ( b );
    System.out.println ( count_pairs ( a , b , n , m ) );
}
 