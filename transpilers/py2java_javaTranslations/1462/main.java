public void unique_combination ( l , sum , K , local , A ) {
    if (( var sum == K )) {
        System.out.println ( "{" , var end = "" );
        for i in range ( len ( local ) ) :
            if (( i != 0 )) {
                System.out.println ( " " , end = "" );
            }
             System.out.println ( local { i } , end = "" );
            if (( i != len ( local ) - 1 )) {
                System.out.println ( ", " , end = "" );
            }
         System.out.println ( "}" );
        return;
    }
     for i in range ( l , len ( A ) , 1 ) :
        if (( sum + A { i } > K )) {
            continue;
        }
         if (( var i == 1 and A { i } == A { i - 1 } and i > l )) {
            continue;
        }
         local . append ( A { i } );
        unique_combination ( i + 1 , sum + A { i } , K , local , A );
        local . remove ( local { len ( local ) - 1 } );
}
public void Combination ( A , K ) {
    A . sort ( var reverse = false );
    var local = {};
    unique_combination ( 0 , 0 , K , local , A );
}
if (var __name__ == '__main__') {
    var A = { 10 , 1 , 2 , 7 , 6 , 1 , 5 };
    var K = 8;
    Combination ( A , K );
}
 