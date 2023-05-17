import heapq;
import collections.deque;
import enum.Enum;
import sys;
import math;
import _heapq.heappush , heappop;
import copy;
var BIG_NUM = 2000000000;
var HUGE_NUM = 99999999999999999;
var MOD = 1000000007;
var EPS = 0.000000001;
sys . setrecursionlimit ( 100000 );
class Type extends  Enum {
    var UNKOWN = 0;
    var OK = 1;
    var NOT = 2;
}

class Info {
    protected void init__ ( this , arg_a , arg_b , arg_c ) {
        this . var work = { arg_a , arg_b , arg_c };
    }
}
while (true) {
    A , B , var C = map ( int , input ( ) . split ( ) );
    if (A == 0 and B == 0 and C == 0) {
        break;
    }
     var table = { Type . UNKOWN } * ( ( A + B + C ) + 1 );
    var N = int ( input ( ) );
    var info = {};
    for _ in range ( N ) :
        a , b , c , var result = map ( int , input ( ) . split ( ) );
        if (result == 1) {
            table { a } = Type . OK;
            table { b } = Type . OK;
            table { c } = Type . OK;
        }
         else{
            info . append ( Info ( a , b , c ) );
        }
    for i in range ( len ( info ) ) :
        var count = 0;
        var tmp = - 1;
        for k in range ( 3 ) :
            if (table { info [ i } . work { k } ] == Type . OK) {
                count += 1;
            }
             else if (table { info [ i } . work { k } ] == Type . UNKOWN){
                tmp = info { i } . work { k };
            }
        if (count != 2 or tmp == - 1) {
            continue;
        }
         table { tmp } = Type . NOT;
    for i in range ( 1 , ( A + B + C ) + 1 ) :
        if (table { i } == Type . OK) {
            System.out.println ( "1" );
        }
         else if (table { i } == Type . NOT){
            System.out.println ( "0" );
        }
        else{
            System.out.println ( "2" );
        }
}
 