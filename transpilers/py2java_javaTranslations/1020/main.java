var MAX = 100;
public void countSubsequence ( s , n ) {
    var cntG = 0;
    var cntF = 0;
    var result = 0;
    var C = 0;
    for i in range ( n ) :
        if (( s { i } == 'G' )) {
            cntG += 1;
            result += C;
            continue;
        }
         if (( s { i } == 'F' )) {
            cntF += 1;
            C += cntG;
            continue;
        }
         else{
            continue;
        }
    System.out.println ( result );
}
if (var __name__ == '__main__') {
    var s = "GFGFG";
    var n = len ( s );
    countSubsequence ( s , n );
}
 