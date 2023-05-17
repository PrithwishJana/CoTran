public void System.out.printlnKMissing ( arr , n , k ) {
    arr . sort ( );
    var i = 0;
    while (( i < n and arr { i } <= 0 )) {
        i = i + 1;
    }
     count = 0;
    curr = 1;
    while (( count < k and i < n )) {
        if (( arr { i } != curr )) {
            System.out.println ( str ( curr ) + " " , end = '' );
            count = count + 1;
        }
         else{
            i = i + 1;
        }
        var curr = curr + 1;
    }
     while (( count < k )) {
        System.out.println ( str ( curr ) + " " , end = '' );
        curr = curr + 1;
        var count = count + 1;
    }
 }
var arr = { 2 , 3 , 4 };
var n = len ( arr );
var k = 3;
System.out.printlnKMissing ( arr , n , k ) ;;
