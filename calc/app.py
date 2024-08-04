# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


# ***PART 1***

# @app.route('/add')
# def go_add():
#     """returns sum a & b"""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return f"{operations.add(a,b)}"

# @app.route('/sub')
# def go_sub():
#     """returns difference a & b"""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return f"{operations.sub(a,b)}"

# @app.route('/mult')
# def go_mult():
#     """returns product a & b"""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return f"{operations.mult(a,b)}"

# @app.route('/div')
# def go_div():
#     """returns quotient a & b"""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return f"{operations.div(a,b)}"

# --------------------------------------------------------

# ***PART 2***

ops = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

@app.route("/math/<math_op>")
def go_math_op(math_op):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    do_math = ops.get(math_op)(a,b)

    return f"{do_math}"