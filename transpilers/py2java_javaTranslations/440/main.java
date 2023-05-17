import numpy as np;
var SIZE = 26;
public void longSub ( str , k ) {
    var freq = np . zeros ( 26 , dtype = np . int );
    var start = 0;
    maxLen = 0;
    n = len ( str );
    for i in range ( 0 , n ) :
        ch = str { i };
        freq { ord ( ch ) - ord ( 'a' ) } += 1;
        if (( freq { ord ( ch ) - ord ( 'a' ) } > k )) {
            if (( maxLen < ( i - start ) )) {
                maxLen = i - start;
            }
             while (( freq { ord ( ch ) - ord ( 'a' ) } > k )) {
                freq { ord ( str [ start } ) - ord ( 'a' ) ] -= 1;
                start = start + 1;
            }
        }
      if (( maxLen < ( n - start ) )) {
        var maxLen = n - start;
     }
     return maxLen ;;
}
var str = "babcaag";
var k = 1;
System.out.println ( "var Length =" , longSub ( str , k ) );
