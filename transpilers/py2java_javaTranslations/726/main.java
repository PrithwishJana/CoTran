public void countPairs ( a , b , n , m ) {
    var cnt = 0;
    var s = dict ( );
    for i in range ( n ) :
        for j in range ( m ) :
            var sum = a { i } + b { j };
            if (( sum not in s . keys ( ) )) {
                cnt += 1;
                s { sum } = 1;
            }
     return cnt;
}
var a = { 12 , 2 , 7 };
var n = len ( a );
var b = { 4 , 3 , 8 };
var m = len ( b );
System.out.println ( countPairs ( a , b , n , m ) );
