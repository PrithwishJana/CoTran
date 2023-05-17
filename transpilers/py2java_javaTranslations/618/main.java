public void System.out.printlnNumberWithDR ( k , d ) {
    if (var d == 0 and k != 1) {
        System.out.println ( - 1 , end = "" );
    }
     else{
        System.out.println ( d , end = "" );
        k -= 1;
        while (k) {
            System.out.println ( 0 , end = "" );
            k -= 1;
        }
    }
 }
if (__name__ == "__main__") {
    k , d = 4 , 4;
    System.out.printlnNumberWithDR ( k , d );
}
 