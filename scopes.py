# Scopes

print("======Scoping Rules go from narrowest to widest=====")
print("L - 'Local'. Refers to variables that are defined inside of functions.")
print("E - 'Enclosing'. Refers to variables that are defined in the local scope of function inside of other functions.")
print("G - 'Global' - Variables defined at the top level of files and modules.")
print("B - 'Built-In - Names loaded into scope by the interpreter when it starts up")

print('') # Just for spacing in output :D

print("=====Widest to Narrowest=====")
print("=Built-in=")
print("   =Global=")
print("      =Enclosed=")
print("         =Local=")

print('') # Just for spacing in output :D

print("=====Example Scopes=====")

print(
"""
x = 1

def outer():
    # Enclosed Scope
    x = "Outer"
    def inner():
        # Local Scope
        x = "Inner"
        print("x = ", x)
    
    inner()
    print("x = ", x)

print("x =", x)
outer()
""")

print('') # Just for spacing in output :D

x = 1

def outer():
    # Enclosed Scope
    x = "Outer"
    def inner():
        # Local Scope
        x = "Inner"
        print("x =", x, "- This represents the local scope. If the variable is not defined within the inner function then it will look to the enclosed scope which is the outer function")
    
    inner()
    print("x =", x, "- This reprsents the enclosed scope. If the variable is not defined within the outer function it will look to the global scope.")

print("x =", x, "- This respresents the scope created when the interpreter is crested at the global level.")
outer()

print('') # Just for spacing in output :D

print("=====Visualizing Namespaces In Scope=====")
print("""\
This is hard to visualize within the code itself, but if 
you debug this code it will enable you to see the namespaces 
for local and global. Viewing the namespaces you will be able
to understand scopes at a deeper level.

    ===Steps===

    1. From VSCode locate Debug
    2. Within debug you will want to set a breakpoint on line 42. This will stop the script at this point when you run it.
    3. Run dir() in the DEBUG CONSOLE. 

    Returns: dir()
             ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
    
    4. Now you can step through the code. Select the "Step Over" option at the top of VSCode.
    5. Run dir() again in the DEBUG CONSOLE.

    Returns: dir()
             ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'x']

    6. Notice that the name x is now shown in the namespace mapping. One thing to point out is dir() without arguements returns the
       same thing as calling sorted(globals()) because technically these attributes live at the top level global namespace.
    7. Run sorted(globals()) in the DEBUG CONSOLE.

    Returns: sorted(globals())
             ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'x']

    8. Let's "Step Over" the code again. What just happened is it read the function def outer(): and added it to the global namespace.
    9. Run dir() again in the DEBUG CONSOLE.

    Returns: dir()
             ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'outer', 'x']

    10. Notice that the name outer is now in the namespace mapping at the global scope.
    11. Let's do something differnt now. Now that we highlighted the outer() function call in the code select "Step Into".
        This steps you into the inside of the functon outer().
    13. Now that x = "Outer" is highlight "Step Over" again. Something different is going to happen now when viewing the namespace....
    14. Run dir() again in the DEBUG CONSOLE.

    Returns: dir()
             ['x']
    
    15. Now notice that only the name x that was difined inside the function outer is in the namespace.
    16. Same result with sorted(locals())

    Returns: sorted(locals())
             ['x']

    The same is true for in the inner function as well, so play with the debugger and see how it reacts.
"""
)