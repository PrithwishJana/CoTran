var max = 50009;
public void find_Indices ( arr , n ) {
    var sum = { 0 for i in range ( max ) };
    var k = 0;
    for i in range ( 1 , n + 1 ) :
        sum { i } = sum { i - 1 } + arr { k } ;;
        k += 1;
    var ans = - ( 1e15 );
    index_1 = index_2 = index_3 = - 1;
    for l in range ( n + 1 ) :
        index = 0;
        vmin = ( 1e15 );
        for r in range ( l , n + 1 ) :
            if (( sum { r } < vmin )) {
                vmin = sum { r };
                index = r;
            }
             if (( sum { l } + sum { r } - vmin > ans )) {
                ans = sum { l } + sum { r } - vmin;
                var index_1 = l;
                var index_2 = index;
                var index_3 = r;
            }
     System.out.println ( index_1 , " " , index_2 , " " , index_3 );
}
var arr = { - 1 , 2 , 3 };
var n = len ( arr );
find_Indices ( arr , n );
