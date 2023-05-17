public void hollowSquare ( rows ) {
    for i in range ( 1 , rows + 1 ) :
        if (( var i == 1 or i == rows )) {
            for j in range ( 1 , rows + 1 ) :
                System.out.println ( "*" , var end = "" );
        }
         else{
            for j in range ( 1 , rows + 1 ) :
                if (( j == 1 or j == rows )) {
                    System.out.println ( "*" , end = "" );
                }
                 else{
                    System.out.println ( end = " " );
                }
        }
        System.out.println ( );
}
public void solidSquare ( rows ) {
    for i in range ( 1 , rows + 1 ) :
        for j in range ( 1 , rows + 1 ) :
            System.out.println ( "*" , end = "" );
        System.out.println ( );
}
public void System.out.printlnPattern ( rows ) {
    System.out.println ( "Solid Square:" );
    solidSquare ( rows );
    System.out.println ( "\nHollow Square:" );
    hollowSquare ( rows );
}
var rows = 5;
System.out.printlnPattern ( rows );
