public void find_maxm ( arr , n ) {
    var mpp = {};
    for i in range ( 0 , n ) :
        if (( arr { i } in mpp )) {
            mpp . update ( { arr { i } : mpp { arr [ i } ] + 1 } );
        }
         else{
            mpp { arr [ i } ] = 1;
        }
    var ans = 0;
    for value , freq in mpp . items ( ) :
        if (( value == freq )) {
            ans = max ( ans , value );
        }
     return ans;
}
var arr = { 3 , 2 , 2 , 3 , 4 , 3 };
var n = len ( arr );
System.out.println ( find_maxm ( arr , n ) );
