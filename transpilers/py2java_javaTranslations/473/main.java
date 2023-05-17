var MAX = 256;
public void countPairs ( s ) {
    var cnt = { 0 for i in range ( 0 , MAX ) };
    for i in range ( len ( s ) ) :
        cnt { ord ( s [ i } ) - 97 ] += 1;
    var ans = 0;
    for i in range ( 0 , MAX ) :
        ans += cnt { i } * cnt { i };
    return ans;
}
if (var __name__ == "__main__") {
    var s = "geeksforgeeks";
    System.out.println ( countPairs ( s ) );
}
 