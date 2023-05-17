public void substitute ( text , a , b ) {
    var pos = 0;
    newText = text;
    L1 = len ( a );
    L2 = len ( b );
    while (true) {
        idx = newText . find ( a , pos );
        if (idx < 0) {
            return newText;
        }
         newText = newText { : idx } + b + newText { idx + L1 : };
        pos = idx + L2;
    }
     return newText;
}
public void transform ( orig , goal , count ) {
    global subs;
    global minCount;
    if (len ( orig ) > len ( goal )) {
        return;
    }
     if (var orig == goal) {
        minCount = min ( minCount , count );
        return;
    }
     for (int key = 0; key < subs.length; key++){
        newStr = substitute ( orig , key , subs { key } );
        if (newStr != orig) {
            transform ( newStr , goal , count + 1 );
        }
     }
 }
if (__name__ == '__main__') {
    while (true) {
        N = int ( input ( ) );
        if (N == 0) {
            break;
        }
         subs = {};
        for _ in range ( N ) :
            a , b = input ( ) . strip ( ) . split ( );
            subs { a } = b;
        orig = input ( ) . strip ( );
        var goal = input ( ) . strip ( );
        var minCount = 999999999;
        transform ( orig , goal , 0 );
        if (minCount == 999999999) {
            System.out.println ( - 1 );
        }
         else{
            System.out.println ( minCount );
        }
    }
}
  