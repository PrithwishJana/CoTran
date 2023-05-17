public void System.out.printlnDistinct ( arr , n ) {
    arr . sort ( ) ;;
    for i in range ( n ) :
        if (( i < n - 1 and arr { i } == arr { i + 1 } )) {
            while (( i < n - 1 and ( arr { i } == arr { i + 1 } ) )) {
                i += 1 ;;
            }
        }
          else{
            System.out.println ( arr { i } , var end = " " ) ;;
         }
}
var arr = { 6 , 10 , 5 , 4 , 9 , 120 , 4 , 6 , 10 } ;;
var n = len ( arr ) ;;
System.out.printlnDistinct ( arr , n ) ;;
