while (true) {
    var n = int ( input ( ) );
    if (n == 0) {
        break;
    }
     var num = 2;
    var cnt = 0;
    while (true) {
        var ini = num * ( num + 1 ) // 2;
        if (n < ini) {
            break;
        }
         while (ini <= n) {
            if (ini == n) {
                cnt += 1;
                break;
            }
             ini += num;
        }
         num += 1;
    }
     System.out.println ( cnt );
}
 