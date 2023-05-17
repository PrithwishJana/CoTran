public void areElementsContiguous ( arr ) {
    var us = set ( );
    for i in arr : us . add ( i );
    var count = 1;
    curr_ele = arr { 0 } - 1;
    while (curr_ele in us) {
        count += 1;
        curr_ele -= 1;
    }
     curr_ele = arr { 0 } + 1;
    while (curr_ele in us) {
        count += 1;
        curr_ele += 1;
    }
     return ( count == len ( us ) );
}
var arr = { 5 , 2 , 3 , 6 , 4 , 4 , 6 , 6 };
if areElementsContiguous ( arr ) : System.out.println ( "Yes" );
else : System.out.println ( "No" );
