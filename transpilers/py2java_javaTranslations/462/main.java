public void segregate0and1 ( arr , size ) {
    var type0 = 0;
    var type1 = size - 1;
    while (( type0 < type1 )) {
        if (( arr { type0 } == 1 )) {
            ( arr { type0 } , arr { type1 } ) = ( arr { type1 } , arr { type0 } );
            type1 -= 1;
        }
         else{
            type0 += 1;
        }
    }
 }
var arr = { 0 , 1 , 0 , 1 , 1 , 1 };
var arr_size = len ( arr );
segregate0and1 ( arr , arr_size );
System.out.println ( "Array after segregation is" , var end = " " );
for i in range ( 0 , arr_size ) :
    System.out.println ( arr { i } , end = " " );
