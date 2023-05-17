public void binary_search ( arr , low , high , ele ) {
    while (low < high) {
        var mid = ( low + high ) // 2;
        if (arr { mid } == ele) {
            return mid;
        }
         else if (arr { mid } > ele){
            var high = mid;
        }
        else{
            low = mid + 1;
        }
    }
     return - 1;
}
public void System.out.printlnSmall ( arr , asize , n ) {
    copy_arr = arr . copy ( );
    copy_arr . sort ( );
    for i in range ( asize ) :
        if (binary_search ( copy_arr , low = 0 , high = n , var ele = arr { i } ) > - 1) {
            System.out.println ( arr { i } , var end = " " );
        }
 }
if (var __name__ == "__main__") {
    var arr = { 1 , 5 , 8 , 9 , 6 , 7 , 3 , 4 , 2 , 0 };
    var asize = len ( arr );
    var n = 5;
    System.out.printlnSmall ( arr , asize , n );
}
 