var INT_MAX = 100000000;
public void minimalSteps ( s , n ) {
    var dp = { INT_MAX for i in range ( n ) };
    var s1 = "";
    s2 = "";
    dp { 0 } = 1;
    s1 += s { 0 };
    for i in range ( 1 , n ) :
        s1 += s { i };
        s2 = s { i + 1 : i + 1 + i + 1 };
        dp { i } = min ( dp { i } , dp { i - 1 } + 1 );
        if (( s1 == s2 )) {
            dp { i * 2 + 1 } = min ( dp { i } + 1 , dp { i * 2 + 1 } );
        }
     return dp { n - 1 };
}
var s = "aaaaaaaa";
var n = len ( s );
System.out.println ( minimalSteps ( s , n ) );
