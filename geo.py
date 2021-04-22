import matplotlib.pyplot as plt
def main():
    x = []
    p = 0.5
    n = 50
    for i in range(n):
        x.append(p*(1-p)**i)
        c = []
        for i in range(len(x)):
            c.append(sum(x[:i+1]))
            plt.figure("cdf")
            plt.plot(range(n), x)
            plt.scatter(range(n), x)
            plt.figure("cdf")
            plt.plot(range(n), c)
            plt.scatter(range(n), c)
            plt.show()
main()
