from interpreterv3 import Interpreter

test10 = [
'func ifunc n:int int',
' return n',
'endfunc',
'',
'func sfunc s:string string',
' return s',
'endfunc',
'',
'func bfunc b:bool bool',
' return b',
'endfunc',
'',
'func main void',
'  var int i',
'  var string s',
'  var bool b',
'  var func f g h',
'  assign f ifunc',
'  assign g sfunc',
'  assign h bfunc',
'',
'  funccall f 42',
'  assign i resulti',
'  funccall print i',
'',
'  funccall g "foo"',
'  assign s results',
'  funccall print s',
'',
'  funccall h True',
'  assign b resultb',
'  funccall print b',
'',
'endfunc',
]

test1 = [
'func main void',
' var func a',
' assign a foo',
'endfunc',
'',
'func foo void',
' return',
'endfunc'
]

test2 = [
'func main void',
' var object a',
' assign a.a "test"',
' assign a.b 0',
' assign a.c False',
' var object b',
' assign b a',
' assign b.a "testing"',
' assign a.d foo',
' funccall print a.a',
' funccall print a.b',
' funccall print a.c',
' funccall b.d',
'endfunc',
'',
'func foo void',
' funccall print "Function foo reached"',
'endfunc'
]

machine = Interpreter()
machine.run(test2)