import collections.defaultdict;
public void maxLenSub ( arr , n ) {
    var um = defaultdict ( lambda : 0 );
    var maxLen = 0;
    for i in range ( 0 , n ) :
        length = 0;
        if (( arr { i } - 1 ) in um and length < um { arr [ i } - 1 ]) {
            length = um { arr [ i } - 1 ];
        }
         if (arr { i } in um and length < um { arr [ i } ]) {
            length = um { arr [ i } ];
        }
         if (( arr { i } + 1 ) in um and length < um { arr [ i } + 1 ]) {
            length = um { arr [ i } + 1 ];
        }
         um { arr [ i } ] = length + 1;
        if (maxLen < um { arr [ i } ]) {
            maxLen = um { arr [ i } ];
        }
     return maxLen;
}
if (var __name__ == "__main__") {
    var arr = { 2 , 5 , 6 , 3 , 7 , 6 , 5 , 8 };
    var n = len ( arr );
    System.out.println ( "Maximum length var subsequence =" , maxLenSub ( arr , n ) );
}
 