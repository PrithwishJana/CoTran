import sys , io , math;
import tokenize.Triple;
import math.*;
var I = lambda : { * map ( int , sys . stdin . readline ( ) . split ( ) ) };
var IS = lambda : input ( );
var IN = lambda : int ( input ( ) );
var IF = lambda : float ( input ( ) );
var days = { 28 , 30 , 31 };
var week = { 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday' };
var a = IS ( );
var b = IS ( );
for index , name in enumerate ( week ) :
    if (var name == a) {
        var ind = index;
    }
 var flag = false;
for (int mo = 0; mo < days.length; mo++){
    if (week { ( ind + mo ) % 7 } == b) {
        flag = true;
    }
}
 if (flag) {
    System.out.println ( 'YES' );
}
 else{
    System.out.println ( 'NO' );
}
