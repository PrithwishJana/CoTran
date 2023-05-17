public void indexOfFirstOne ( arr , low , high ) {
    while (( low <= high )) {
        var mid = ( low + high ) // 2;
        if (( arr { mid } == 1 and ( mid == 0 or arr { mid - 1 } == 0 ) )) {
            break;
        }
         else if (( arr { mid } == 1 )){
            var high = mid - 1;
        }
        else{
            var low = mid + 1;
        }
    }
     return mid;
}
public void posOfFirstOne ( arr ) {
    var l = 0;
    h = 1;
    while (( arr { h } == 0 )) {
        l = h;
        var h = 2 * h;
    }
     return indexOfFirstOne ( arr , l , h );
}
var arr = { 0 , 0 , 1 , 1 , 1 , 1 };
System.out.println ( "var Index = " , posOfFirstOne ( arr ) );
