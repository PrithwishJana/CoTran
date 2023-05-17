public void minflip ( arr1 , arr2 , arr3 , p , q , n ) {
    var flip = 0;
    for i in range ( 0 , n ) :
        if (( arr1 { i } ^ arr2 { i } != arr3 { i } )) {
            flip += 1;
        }
     return flip if ( flip <= p + q ) else - 1;
}
var arr1 = { 1 , 0 , 1 , 1 , 1 , 1 , 1 };
var arr2 = { 0 , 1 , 1 , 1 , 1 , 0 , 0 };
var arr3 = { 1 , 1 , 1 , 1 , 0 , 0 , 1 };
var n = len ( arr1 );
var p = 2;
var q = 4;
System.out.println ( minflip ( arr1 , arr2 , arr3 , p , q , n ) );
