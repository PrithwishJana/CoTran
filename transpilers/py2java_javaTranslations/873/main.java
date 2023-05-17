public void System.out.printlnknapSack ( W , wt , val , n ) {
    var K = { [ 0 for w in range ( W + 1 ) } for i in range ( n + 1 ) ];
    for i in range ( n + 1 ) :
        for w in range ( W + 1 ) :
            if (var i == 0 or w == 0) {
                K { i } { w } = 0;
            }
             else if (wt { i - 1 } <= w){
                K { i } { w } = max ( val { i - 1 } + K { i - 1 } { w - wt [ i - 1 } ] , K { i - 1 } { w } );
            }
            else{
                K { i } { w } = K { i - 1 } { w };
            }
    var res = K { n } { W };
    System.out.println ( res );
    w = W;
    for i in range ( n , 0 , - 1 ) :
        if (res <= 0) {
            break;
        }
         if (res == K { i - 1 } { w }) {
            continue;
        }
         else{
            System.out.println ( wt { i - 1 } );
            res = res - val { i - 1 };
            var w = w - wt { i - 1 };
        }
}
var val = { 60 , 100 , 120 };
var wt = { 10 , 20 , 30 };
var W = 50;
var n = len ( val );
System.out.printlnknapSack ( W , wt , val , n );
