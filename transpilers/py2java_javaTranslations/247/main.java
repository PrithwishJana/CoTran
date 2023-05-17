var lis = {};
var cnt = 0;
while (true) {
    try{
        var n = int ( input ( ) );
        if (n) {
            cnt += 1;
            lis . append ( n );
        }
         else{
            System.out.println ( lis . pop ( cnt - 1 ) );
            cnt -= 1;
        }
    }
    except :
        break;
}
 