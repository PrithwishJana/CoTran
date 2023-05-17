import sys;
public void main ( ) {
    var n = int ( sys . stdin . readline ( ) . strip ( '\n' ) );
    var taro_score = 0;
    var hanako_score = 0;
    for turn in range ( n ) :
        var animals = { animal for animal in sys . stdin . readline ( ) . strip ( '\n' ) . split ( ' ' ) };
        if (animals { 0 } == animals { 1 }) {
            taro_score += 1;
            hanako_score += 1;
        }
         else if (max ( animals { 0 } , animals { 1 } ) == animals { 0 }){
            taro_score += 3;
        }
        else if (max ( animals { 0 } , animals { 1 } ) == animals { 1 }){
            hanako_score += 3;
        }
    System.out.println ( '%d %d' % ( taro_score , hanako_score ) );
}
if (var __name__ == '__main__') {
    main ( );
}
 