public void AlternateRearrange ( arr , n ) {
    arr . sort ( );
    var v1 = list ( );
    var v2 = list ( );
    for i in range ( n ) :
        if (( arr { i } % var 2 == 0 )) {
            v1 . append ( arr { i } );
        }
         else{
            v2 . append ( arr { i } );
        }
    index = 0;
    i = 0;
    j = 0;
    flag = false;
    if (( arr { 0 } % 2 == 0 )) {
        var flag = true;
    }
     while (( index < n )) {
        if (( flag == true )) {
            arr { index } = v1 { i };
            index += 1;
            i += 1;
            flag = ~ flag;
        }
         else{
            arr { index } = v2 { j };
            index += 1;
            j += 1;
            flag = ~ flag;
        }
    }
     for i in range ( n ) :
        System.out.println ( arr { i } , var end = " " );
}
var arr = { 9 , 8 , 13 , 2 , 19 , 14 };
var n = len ( arr );
AlternateRearrange ( arr , n );
