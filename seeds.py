from app import app, db
from models.code_thing import CodeThing

with app.app_context():
    db.drop_all()
    db.create_all()



functional_programming = CodeThing(
    type='Paradigm',
    name='Functional Programming',
    explanation='Functional programming (often abbreviated FP) is the process of building software by composing pure functions, avoiding shared state, mutable data, and side-effects. Functional programming is declarative rather than imperative. Contrast with object oriented programming, where application state is usually shared and colocated with methods in objects.',
    link='https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming'

)

pure_function = CodeThing(
    type='Function Type',
    name='Pure Function',
    explanation='A pure function is a function which given the same input, will always return the same output and produces no side effects',
    example='Lily-La-Day/7456efd69c5d0b2292cd5b887adba436',
    link='https://www.geeksforgeeks.org/pure-functions/'
)

curried_function = CodeThing(
    type='Function Type',
    name='Curried Function',
    explanation='A curried function is a function that takes multiple arguments one at a time. Currying is translating a function that takes multiple arguments into a sequence of functions, each accepting one argument.',
    example='Lily-La-Day/ef4b1dce75225b7ee9db7466f17b5afa',
    link='https://medium.com/@kbrainwave/currying-in-javascript-ce6da2d324fe'
)

function_composition = CodeThing(
    type='Function Type',
    name='Function Composition',
    explanation='Function composition is a mathematical concept that allows us to combine two or more functions into a new function. Functions are taken and a new function is returned that automates the passing of input and output between those functions.',
    example='Lily-La-Day/ee8a649ead0ae61b0efb81004d97d441',
    link='http://blog.ricardofilipe.com/post/javascript-composition-for-dummies'
)



higher_order_function = CodeThing(
    type='Function Type',
    name='Higher Order Function',
    explanation='Functions that operate on other functions, either by taking them as arguments or by returning them.',
    example='Lily-La-Day/ef1415e7c8d7af3f71f60eb0fe4d4e32',
    link='https://eloquentjavascript.net/05_higher_order.html'
)

shared_state = Code_Thing(
    type='Concept',
    name='Shared State',
    explanation='A shared state is any variable, object, or memory space that exists in a shared scope. Any non-constant variable used by multiple separate scopes, including the global scope and closure scopes, is considered to be in a shared state. In functional programming, shared states should be avoided.  ',
    link='https://www.quora.com/What-is-the-meaning-of-shared-state-and-the-side-effects-in-functional-programming'
)

closure = Code_Thing(
    type='Concept',
    name='Closure',
    explanation='A closure is a persistent scope which holds on to local variables even after the code execution has moved out of that block.',
    link='https://stackoverflow.com/questions/36636/what-is-a-closure'

)

big_o_notation = Code_Thing(

)



promise = Code_Thing(

)


db.session.add(functional_programming)
db.session.add(pure_function)
db.session.add(curried_function)
db.session.add(function_composition)
db.session.add(higher_order_function)

db.session.commit()
