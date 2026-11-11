# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” and see the effects.

# Answer is Yes we can change the self parameter to any of the other like slf or anything else.
class Demo :
    
    def __init__(slf,name):
        slf.name = name

    def greet(slf):
        print(f"Good Day {slf.name}")


d = Demo("Suman")
d.greet()
        # Its still running good.