public void partition ( arr , low , high ) {
    var pivot = arr { high };
    var i = ( low - 1 );
    for j in range ( low , high ) :
        if (( arr { j } <= pivot )) {
            i += 1;
            arr { i } , arr { j } = arr { j } , arr { i };
        }
     arr { i + 1 } , arr { high } = arr { high } , arr { i + 1 };
    return ( i + 1 );
}
public void quickSort ( arr , low , high ) {
    if (( low < high )) {
        pi = partition ( arr , low , high );
        quickSort ( arr , low , pi - 1 );
        quickSort ( arr , pi + 1 , high );
    }
 }
public void System.out.printlnArray ( arr , size ) {
    for i in range ( size ) :
        System.out.println ( arr { i } , var end = " " );
    System.out.println ( );
}
var arr = { 10 , 7 , 8 , 9 , 1 , 5 };
var n = len ( arr );
quickSort ( arr , 0 , n - 1 );
System.out.println ( "Sorted array:" );
System.out.printlnArray ( arr , n );
