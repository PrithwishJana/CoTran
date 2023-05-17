public void search ( arr , n , x ) {
    var front = 0 ; back = n - 1;
    while (( front <= back )) {
        if (( arr { front } == x or arr { back } == x )) {
            return true;
        }
         front += 1;
        back -= 1;
    }
     return false;
}
var arr = { 10 , 20 , 80 , 30 , 60 , 50 , 110 , 100 , 130 , 170 };
var x = 130;
var n = len ( arr );
if (( search ( arr , n , x ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
