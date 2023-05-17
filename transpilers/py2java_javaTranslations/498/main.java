public void isMajority ( a ) {
    var mp = {};
    for (int i = 0; i < a.length; i++){
        if i in mp : mp { i } += 1;
        else : mp { i } = 1;
    }
    for (int x = 0; x < mp.length; x++){
        if (mp { x } >= len ( a ) // 2) {
            return true;
        }
    }
     return false;
}
var a = { 2 , 3 , 9 , 2 , 2 };
System.out.println ( "Yes" if isMajority ( a ) else "No" );
