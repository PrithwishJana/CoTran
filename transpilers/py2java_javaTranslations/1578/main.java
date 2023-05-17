import collections.defaultdict;
public void longLenSub ( arr , n ) {
    var um = defaultdict ( lambda : 0 );
    var longLen = 0;
    for i in range ( n ) :
        len1 = 0;
        if (( arr { i - 1 } in um and len1 < um { arr [ i } - 1 ] )) {
            len1 = um { arr [ i } - 1 ];
        }
         if (( arr { i } + 1 in um and len1 < um { arr [ i } + 1 ] )) {
            len1 = um { arr [ i } + 1 ];
        }
         um { arr [ i } ] = len1 + 1;
        if (longLen < um { arr [ i } ]) {
            longLen = um { arr [ i } ];
        }
     return longLen;
}
var arr = { 1 , 2 , 3 , 4 , 5 , 3 , 2 };
var n = len ( arr );
System.out.println ( "Longest length var subsequence =" , longLenSub ( arr , n ) );
