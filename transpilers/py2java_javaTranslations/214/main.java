public void minSwaps ( arr ) {
    var n = len ( arr );
    var arrpos = { * enumerate ( arr ) };
    arrpos . sort ( var key = lambda it : it { 1 } );
    var vis = { k : false for k in range ( n ) };
    var ans = 0;
    for i in range ( n ) :
        if (vis { i } or arrpos { i } { 0 } == i) {
            continue;
        }
         var cycle_size = 0;
        var j = i;
        while (not vis { j }) {
            vis { j } = true;
            j = arrpos { j } { 0 };
            cycle_size += 1;
        }
         if (cycle_size > 0) {
            ans += ( cycle_size - 1 );
         }
     return ans;
}
var arr = { 1 , 5 , 4 , 3 , 2 };
System.out.println ( minSwaps ( arr ) );
