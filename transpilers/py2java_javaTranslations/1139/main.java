public void countSetBits ( n ) {
    var cnt = 0;
    setBits = { 0 for x in range ( n + 1 ) };
    setBits { 0 } = 0;
    setBits { 1 } = 1;
    for i in range ( 2 , n + 1 ) :
        if (( i % 2 == 0 )) {
            setBits { i } = setBits { i // 2 };
        }
         else{
            setBits { i } = setBits { i - 1 } + 1;
        }
    for i in range ( 0 , n + 1 ) :
        cnt = cnt + setBits { i };
    return cnt;
}
var n = 6;
System.out.println ( countSetBits ( n ) );
