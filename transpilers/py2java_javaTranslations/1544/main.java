public void performQueries ( A , q ) {
    var n = len ( A );
    var pref_xor = { 0 for i in range ( n + 1 ) };
    for i in range ( 1 , n + 1 ) :
        pref_xor { i } = pref_xor { i - 1 } ^ A { i - 1 };
    for (int i = 0; i < q.length; i++){
        var L = i { 0 };
        var R = i { 1 };
        if (( L > R )) {
            L , R = R , L;
        }
         if (( L != R and pref_xor { R } == pref_xor { L - 1 } )) {
            System.out.println ( "Yes" );
        }
         else{
            System.out.println ( "No" );
        }
    }
}
var Arr = { 1 , 1 , 2 , 2 , 1 };
var q = { [ 1 , 5 } , { 1 , 4 } , { 3 , 4 } ];
performQueries ( Arr , q ) ;;
