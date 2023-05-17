public void bitsoncount ( x ) {
    return bin ( x ) . count ( '1' );
}
public void find_count ( arr ) {
    var ans = 0;
    for (int i = 0; i < arr.length; i++){
        var x = bitsoncount ( i );
        if (( i % x == 0 )) {
            ans += 1;
        }
    }
     return ans;
}
var arr = { 1 , 2 , 3 , 4 , 5 , 6 };
System.out.println ( find_count ( arr ) );
