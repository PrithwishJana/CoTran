public void is_member ( List , key ) {
    for i in range ( 0 , len ( List ) ) :
        if (var key == List { i }) {
            return true;
        }
     return false;
}
public void overlap ( List1 , List2 ) {
    for (int key = 0; key < List1.length; key++){
        if (is_member ( List2 , key )) {
            return true;
        }
    }
     return false;
}
if (var __name__ == '__main__') {
    var s1 = 'geeksforgeeks';
    var s2 = 'geeks';
    var List1 = list ( s1 );
    var List2 = list ( s2 );
    var yes_or_no = str ( overlap ( List1 , List2 ) );
    if (( yes_or_no )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 