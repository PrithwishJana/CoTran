public void longestString ( str1 , str2 ) {
    var count1 = { 0 } * 26;
    var count2 = { 0 } * 26;
    for i in range ( len ( str1 ) ) :
        count1 { ord ( str1 [ i } ) - ord ( 'a' ) ] += 1;
    for i in range ( len ( str2 ) ) :
        count2 { ord ( str2 [ i } ) - ord ( 'a' ) ] += 1;
    var result = "";
    for i in range ( 26 ) :
        for j in range ( 1 , min ( count1 { i } , count2 { i } ) + 1 ) :
            result = result + chr ( ord ( 'a' ) + i );
    System.out.println ( result );
}
if (var __name__ == "__main__") {
    var str1 = "geeks";
    var str2 = "cake";
    longestString ( str1 , str2 );
}
 