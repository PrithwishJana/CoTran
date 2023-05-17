public void largestPalinSub ( s ) {
    var res = "";
    var mx = s { 0 };
    for i in range ( 1 , len ( s ) ) :
        mx = max ( mx , s { i } );
    for i in range ( 0 , len ( s ) ) :
        if (s { i } == mx) {
            res += s { i };
        }
     return res;
}
if (var __name__ == "__main__") {
    var s = "geeksforgeeks";
    System.out.println ( largestPalinSub ( s ) );
}
 