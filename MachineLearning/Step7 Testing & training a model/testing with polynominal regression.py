import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)

plt.scatter(test_x, test_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(test_y, mymodel(test_x)) # < relationship is high meaning results should be accurate
print(r2) # < 0.8086921460343581 very similar to train results

# V prediction of value Y if X is 5
print(mymodel(5)) # 22.87962591811811 < same result as train
