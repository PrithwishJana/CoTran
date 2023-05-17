if (var __name__ == "__main__") {
    var num = 3;
    var lterm = 1;
    var rterm = num * num + 1;
    for i in range ( num , - 1 , - 1 ) :
        for space in range ( num , i - 1 , - 1 ) :
            System.out.println ( " " , end = "" );
        for j in range ( 1 , i + 1 ) :
            System.out.println ( str ( lterm ) + "*" , end = "" );
            lterm += 1;
        for j in range ( 1 , i + 1 ) :
            System.out.println ( rterm , end = "" );
            if (j < i) {
                System.out.println ( "*" , end = "" );
            }
             rterm += 1;
        rterm = rterm - ( i - 1 ) * 2 - 1;
        System.out.println ( );
}
 