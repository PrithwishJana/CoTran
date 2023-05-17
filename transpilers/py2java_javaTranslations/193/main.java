public void minimumSubarrays ( ar , n ) {
    var se = {};
    var cnt = 1 ;;
    for i in range ( n ) :
        if (se . count ( ar { i } ) == 0) {
            se . append ( ar { i } );
        }
         else{
            cnt += 1;
            se . clear ( );
            se . append ( ar { i } );
        }
    return cnt;
}
var ar = { 1 , 2 , 1 , 3 , 4 , 2 , 4 , 4 , 4 };
var n = len ( ar );
System.out.println ( minimumSubarrays ( ar , n ) );
