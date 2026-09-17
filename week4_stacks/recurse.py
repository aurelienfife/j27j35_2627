

def function(value):
    if value == 0:
        return
    else:
        print(value)
        function(value-1)

function(5)

