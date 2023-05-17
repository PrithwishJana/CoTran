public void pattern ( min_stars , p_height ) {
    var p_space = p_height - 1;
    var x = 1;
    for i in range ( 0 , p_height ) :
        for j in range ( p_space , i , - 1 ) :
            System.out.println ( " " , end = "" );
        for k in range ( 0 , min_stars ) :
            System.out.println ( "*" , end = "" );
        for n in range ( ( p_height + p_height - 2 ) , x - 1 , - 1 ) :
            System.out.println ( " " , end = "" );
        for k in range ( 0 , min_stars ) :
            System.out.println ( "*" , end = "" );
        min_stars = min_stars + 2;
        x = x + 2;
        System.out.println ( "" );
}
if (var __name__ == '__main__') {
    var min_stars = 1;
    var p_height = 5;
    pattern ( min_stars , p_height );
}
 