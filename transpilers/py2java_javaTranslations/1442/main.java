public void findFrequencyUtil ( arr , low , high , freq ) {
    if (( arr { low } == arr { high } )) {
        freq { arr [ low } ] += high - low + 1;
    }
     else{
        var mid = int ( ( low + high ) / 2 );
        findFrequencyUtil ( arr , low , mid , freq );
        findFrequencyUtil ( arr , mid + 1 , high , freq );
    }
}
public void findFrequency ( arr , n ) {
    var freq = { 0 for i in range ( n - 1 + 1 ) };
    findFrequencyUtil ( arr , 0 , n - 1 , freq );
    for i in range ( 0 , arr { n - 1 } + 1 , 1 ) :
        if (( freq { i } != 0 )) {
            System.out.println ( "Element" , i , "occurs" , freq { i } , "times" );
        }
 }
if (var __name__ == '__main__') {
    var arr = { 1 , 1 , 1 , 2 , 3 , 3 , 5 , 5 , 8 , 8 , 8 , 9 , 9 , 10 };
    var n = len ( arr );
    findFrequency ( arr , n );
}
 