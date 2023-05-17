class p205:
    @staticmethod
    def main(args):
        print((p205()).run())
    _PYRAMIDAL_DIE_PDF = [0, 1, 1, 1, 1]
    _CUBIC_DIE_PDF = [0, 1, 1, 1, 1, 1, 1]
    def run(self):
        ninePyramidalPdf = [1]
        for i in range(0, 9):
            ninePyramidalPdf = p205._convolve(ninePyramidalPdf, p205._PYRAMIDAL_DIE_PDF)
        sixCubicPdf = [1]
        for i in range(0, 6):
            sixCubicPdf = p205._convolve(sixCubicPdf, p205._CUBIC_DIE_PDF)
        numer = 0
        i = 0
        while i < len(ninePyramidalPdf):
            numer += int(ninePyramidalPdf [i]) * p205._sum(sixCubicPdf, 0, i)
            i += 1
        denom = int(p205._sum(ninePyramidalPdf, 0, len(ninePyramidalPdf))) * p205._sum(sixCubicPdf, 0, len(sixCubicPdf))
        return "{0:.7f}".format(float(numer) / denom)
    @staticmethod
    def _convolve(a, b):
        c = [0 for _ in range(len(a) + len(b) - 1)]
        i = 0
        while i < len(a):
            j = 0
            while j < len(b):
                c [i + j] += a [i] * b [j]
                j += 1
            i += 1
        return c
    @staticmethod
    def _sum(array, start, end):
        sum = 0
        for i in range(start, end):
            sum += array [i]
        return sum
