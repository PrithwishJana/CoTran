public void solve ( i , tight , sum_so_far , Sum , number , length ) {
    if (var i == length) {
        if (var sum_so_far == Sum) {
            return 1;
        }
         else{
            return 0;
        }
    }
     ans = dp { i } { tight } { sum_so_far };
    if (ans != - 1) {
        return ans;
    }
     ans = 0;
    for currdigit in range ( 0 , 10 ) :
        currdigitstr = str ( currdigit );
        if (not tight and currdigitstr > number { i }) {
            break;
        }
         ntight = tight or currdigitstr < number { i };
        nsum_so_far = sum_so_far + currdigit;
        ans += solve ( i + 1 , ntight , nsum_so_far , Sum , number , length );
    return ans;
}
if (var __name__ == "__main__") {
    count , var Sum = 0 , 4;
    var number = "100";
    var dp = { [ [ - 1 for i in range ( 162 ) } for j in range ( 2 ) ] for k in range ( 18 ) ];
    System.out.println ( solve ( 0 , 0 , 0 , Sum , number , len ( number ) ) );
}
 