public void findExtraCharacter ( strA , strB ) {
    var m1 = {};
    for (int i = 0; i < strB.length; i++){
        if (i in m1) {
            m1 { i } += 1;
        }
         else{
            m1 { i } = 1;
        }
    }
    for (int i = 0; i < strA.length; i++){
        m1 { i } -= 1;
    }
    for (int h1 = 0; h1 < m1.length; h1++){
        if (m1 { h1 } == 1) {
            return h1;
        }
    }
 }
if (var __name__ == "__main__") {
    var strA = 'abcd';
    var strB = 'cbdad';
    System.out.println ( findExtraCharacter ( strA , strB ) );
}
 