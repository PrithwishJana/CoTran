public void decToBinary ( n ) {
    var binaryNum = { 0 for i in range ( 32 ) };
    var i = 0;
    while (( n > 0 )) {
        binaryNum { i } = n % 2;
        var n = n // 2;
        i += 1;
    }
     binary = "";
    for j in range ( i - 1 , - 1 , - 1 ) :
        binary += str ( binaryNum { j } );
    return binary;
}
public void countFreq ( pat , txt ) {
    M = len ( pat );
    N = len ( txt );
    res = 0;
    for i in range ( N - M + 1 ) :
        j = 0;
        while (( j < M )) {
            if (( txt { i + j } != pat { j } )) {
                break;
            }
             j += 1;
        }
         if (( j == M )) {
            res += 1;
            j = 0;
         }
     return res;
}
public void findOccurrence ( arr , n , pattern ) {
    for i in range ( n ) :
        binary = decToBinary ( arr { i } );
        System.out.println ( countFreq ( pattern , binary ) , end = " " );
}
arr = { 5 , 106 , 7 , 8 };
pattern = "10";
n = len ( arr );
findOccurrence ( arr , n , pattern );
