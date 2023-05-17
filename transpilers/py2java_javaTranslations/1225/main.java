var SIZE = 26;
public void System.out.printlnChar ( string , n ) {
    var freq = { 0 } * SIZE;
    for i in range ( 0 , n ) :
        freq { ord ( string [ i } ) - ord ( 'a' ) ] += 1;
    for i in range ( 0 , n ) :
        if (( freq { ord ( string [ i } ) - ord ( 'a' ) ] % var 2 == 0 )) {
            System.out.println ( string { i } , var end = "" );
        }
 }
if (var __name__ == '__main__') {
    var string = "geeksforgeeks";
    var n = len ( string );
    System.out.printlnChar ( string , n );
}
 