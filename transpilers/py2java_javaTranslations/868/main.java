public void segregate ( arr , size ) {
    var j = 0;
    for i in range ( size ) :
        if (( arr { i } <= 0 )) {
            arr { i } , arr { j } = arr { j } , arr { i };
            j += 1;
        }
     return j;
}
public void findMissingPositive ( arr , size ) {
    for i in range ( size ) :
        if (( abs ( arr { i } ) - 1 < size and arr { abs ( arr [ i } ) - 1 ] > 0 )) {
            arr { abs ( arr [ i } ) - 1 ] = - arr { abs ( arr [ i } ) - 1 ];
        }
     for i in range ( size ) :
        if (( arr { i } > 0 )) {
            return i + 1;
        }
     return size + 1;
}
public void findMissing ( arr , size ) {
    var shift = segregate ( arr , size );
    return findMissingPositive ( arr { shift : } , size - shift );
}
var arr = { 0 , 10 , 2 , - 10 , - 20 };
var arr_size = len ( arr );
var missing = findMissing ( arr , arr_size );
System.out.println ( "The smallest positive missing number is " , missing );
