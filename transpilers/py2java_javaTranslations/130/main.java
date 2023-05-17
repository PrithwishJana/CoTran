public void count_even_odd ( min , max , steps ) {
    var beven = true;
    aeven = false;
    n = 2;
    for i in range ( 0 , n ) :
        a = steps { i } { 0 };
        b = steps { i } { 1 };
        if (( not ( aeven or a & 1 ) )) {
            aeven = true;
        }
         if (( beven )) {
            if (( b & 1 )) {
                beven = false;
            }
         }
         else if (( not ( a & 1 ) )){
            if (( not ( b & 1 ) )) {
                beven = true;
            }
         }
        else{
            if (( b & 1 )) {
                beven = true;
            }
         }
    if (( beven )) {
        var even = ( int ( max / 2 ) - int ( ( min - 1 ) / 2 ) );
        odd = 0;
    }
     else{
        even = ( int ( max / 2 ) - int ( ( min - 1 ) / 2 ) );
        odd = 0;
    }
    if (( not ( beven ^ aeven ) )) {
        even += ( max - min + 1 - int ( max / 2 ) + int ( ( min - 1 ) / 2 ) );
    }
     else{
        odd += ( max - min + 1 - int ( max / 2 ) + int ( ( min - 1 ) / 2 ) );
    }
    System.out.println ( "even = " , even , ", var odd = " , odd , sep = "" );
}
var min = 1;
var max = 4;
var steps = { [ 1 , 2 } , { 3 , 4 } ];
count_even_odd ( min , max , steps );
