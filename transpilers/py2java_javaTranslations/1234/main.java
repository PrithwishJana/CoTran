import collections;
public void minIncrementForUnique ( A ) {
    var count = collections . Counter ( A );
    var taken = {};
    var ans = 0;
    for x in range ( 100000 ) :
        if (count { x } >= 2) {
            taken . extend ( { x } * ( count { x } - 1 ) );
        }
         else if (taken and count { x } == 0){
            ans += x - taken . pop ( );
        }
    return ans;
}
var A = { 3 , 2 , 1 , 2 , 1 , 7 };
System.out.println ( minIncrementForUnique ( A ) );
