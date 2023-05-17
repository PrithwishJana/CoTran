public void countSetBits ( n ) {
    var count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
     return count;
}
public void countOfOddPascal ( n ) {
    var c = countSetBits ( n );
    return pow ( 2 , c );
}
var n = 20;
System.out.println ( countOfOddPascal ( n ) );
