public void generateDivisors ( curIndex , curDivisor , arr ) {
    if (( var curIndex == len ( arr ) )) {
        System.out.println ( curDivisor , end = ' ' );
        return;
    }
     for i in range ( arr { curIndex } { 0 } + 1 ) :
        generateDivisors ( curIndex + 1 , curDivisor , arr );
        curDivisor *= arr { curIndex } { 1 };
}
public void findDivisors ( n ) {
    arr = {};
    i = 2;
    while (( i * i <= n )) {
        if (( n % i == 0 )) {
            count = 0;
            while (( n % i == 0 )) {
                n //= i;
                count += 1;
            }
             arr . append ( { count , i } );
        }
     }
     if (( n > 1 )) {
        arr . append ( { 1 , n } );
     }
     curIndex = 0;
    var curDivisor = 1;
    generateDivisors ( curIndex , curDivisor , arr );
}
var n = 6;
findDivisors ( n );
