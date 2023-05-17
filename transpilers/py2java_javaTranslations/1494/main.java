public void System.out.printlnDuplicates ( arr , n ) {
    var fl = 0 ;;
    for i in range ( 0 , n ) :
        if (( arr { arr [ i } % n ] >= n )) {
            if (( arr { arr [ i } % n ] < 2 * n )) {
                System.out.println ( arr { i } % n , end = " " );
                fl = 1 ;;
            }
         }
         arr { arr [ i } % n ] += n ;;
    if (( fl == 0 )) {
        System.out.println ( "-1" );
    }
 }
var arr = { 1 , 6 , 3 , 1 , 3 , 6 , 6 } ;;
var arr_size = len ( arr ) ;;
System.out.printlnDuplicates ( arr , arr_size ) ;;
