public void smallest ( s ) {
    var l = len ( s );
    var ans = "";
    for i in range ( l ) :
        if (( s { i } > s { i + 1 } )) {
            for j in range ( l ) :
                if (( i != j )) {
                    ans += s { j };
                }
             return ans;
        }
     ans = s { 0 : l - 1 };
    return ans;
}
if (var __name__ == "__main__") {
    var s = "abcda";
    System.out.println ( smallest ( s ) );
}
 