public void search ( arr , n , x ) {
    for i in range ( 0 , n ) :
        if (( arr { i } == x )) {
            return i ;;
        }
     return - 1 ;;
}
var arr = { 2 , 3 , 4 , 10 , 40 } ;;
var x = 10 ;;
var n = len ( arr ) ;;
var result = search ( arr , n , x );
if (( result == - 1 )) {
    System.out.println ( "Element is not present in array" );
}
 else{
    System.out.println ( "Element is present at index" , result ) ;;
}
