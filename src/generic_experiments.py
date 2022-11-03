import types_builtin as B
#
#
def generic(x: B.T, y: B.T) -> B.T:
#(
    return x
#)


from typing import AnyStr

def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y

concat('a', 'b')    # Okay
concat(b'a', b'b')  # Okay
#concat(1, 2)        # mypy Error!









def main(*args, **kwargs):
#(
    generic(x = [1,2,3] , y = 5)
    generic(x = [1,2,3] , y = "string")
#)


if __name__ == "__main__":
#(
    main()
#)
