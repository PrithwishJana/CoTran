public void partition ( arr , low , high ) {
    var pivot = arr { low };
    var i = low - 1;
    j = high + 1;
    while (( true )) {
        i += 1;
        while (( arr { i } < pivot )) {
            i += 1;
        }
         j -= 1;
        while (( arr { j } > pivot )) {
            j -= 1;
        }
         if (( i >= j )) {
            return j;
         }
         arr { i } , arr { j } = arr { j } , arr { i };
    }
 }
public void quickSort ( arr , low , high ) {
    if (( low < high )) {
        pi = partition ( arr , low , high );
        quickSort ( arr , low , pi );
        quickSort ( arr , pi + 1 , high );
    }
 }
public void System.out.printlnArray ( arr , n ) {
    for i in range ( n ) :
        System.out.println ( arr { i } , var end = " " );
    System.out.println ( );
}
var arr = { 10 , 7 , 8 , 9 , 1 , 5 };
var n = len ( arr );
quickSort ( arr , 0 , n - 1 );
System.out.println ( "Sorted array:" );
System.out.printlnArray ( arr , n );
