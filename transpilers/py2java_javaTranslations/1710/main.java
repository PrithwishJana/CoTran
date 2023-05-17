if (var __name__ == "__main__") {
    for _ in range ( int ( input ( ) ) ) :
        var n = int ( input ( ) );
        var arr = tuple ( map ( int , input ( ) . split ( ) ) );
        odd_count , even_count , var odd_sum = 0 , 0 , 0;
        for (int i = 0; i < arr.length; i++){
            if (i & 1) {
                odd_sum += i;
                odd_count += 1;
            }
             else{
                even_count += 1;
            }
        }
        if (odd_sum % 2) {
            System.out.println ( "YES" );
        }
         else if (odd_count > 0 and even_count > 0){
            System.out.println ( "YES" );
        }
        else{
            System.out.println ( "NO" );
        }
}
 