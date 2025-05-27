import graphics as gr

window = gr.GraphWin("Square", 600, 600)
alpha = 0.2

def drawSquare():
    def fractialRectangle(A, B, C, D, deep=10):
        if deep < 1:
            return
        for M,N in (A,B), (B,C), (C,D), (D,A):
            gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

        A1 = (A[0] * (1 - alpha)) + (B[0] * alpha), (A[1] * (1 - alpha)) + (B[1] * alpha)
        B1 = (B[0] * (1 - alpha)) + (C[0] * alpha), (B[1] * (1 - alpha)) + (C[1] * alpha)
        C1 = (C[0] * (1 - alpha)) + (D[0] * alpha), (C[1] * (1 - alpha)) + (D[1] * alpha)
        D1 = (D[0] * (1 - alpha)) + (A[0] * alpha), (D[1] * (1 - alpha)) + (A[1] * alpha)

        fractialRectangle(A1, B1, C1, D1)

    A = (100, 100)
    B = (500, 100)
    C = (500, 500)
    D = (100, 500)

    fractialRectangle(A, B, C, D)

    # def fractialRectangle(A, B, C, D): 
    #     drawLine(A, B)
    #     drawLine(B, C)
    #     drawLine(C, D)
    #     drawLine(D, A)
    #
    # def drawRectangle2(A,B,C,D):
    #     for m,n in (A,B), (B,C), (C,D), (D,A):
    #         drawLine(m,n)
    #

    window.getMouse()  # Prevents the window from closing immediately
