public void pattern ( rows_no ) {
    for i in range ( 1 , rows_no + 1 ) :
        for k in range ( 1 , i ) :
            System.out.println ( " " , var end = "" );
        for j in range ( i , rows_no + 1 ) :
            System.out.println ( j , end = " " );
        System.out.println ( );
    for i in range ( rows_no - 1 , 0 , - 1 ) :
        for k in range ( 1 , i ) :
            System.out.println ( " " , end = "" );
        for j in range ( i , rows_no + 1 ) :
            System.out.println ( j , end = " " );
        System.out.println ( );
}
var rows_no = 7;
pattern ( rows_no );
