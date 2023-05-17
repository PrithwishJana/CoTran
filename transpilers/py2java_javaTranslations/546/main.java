public void nondecdigits ( n ) {
    var x = 0;
    for x in range ( n , 0 , - 1 ) :
        var no = x;
        var prev_dig = 11;
        flag = true;
        while (( no != 0 )) {
            if (( prev_dig < no % 10 )) {
                flag = false;
                break;
            }
             prev_dig = no % 10;
            no //= 10;
        }
         if (( var flag == true )) {
            break;
         }
     return x;
}
if (var __name__ == "__main__") {
    var n = 200;
    System.out.println ( nondecdigits ( n ) );
}
 