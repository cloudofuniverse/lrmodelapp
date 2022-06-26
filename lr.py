import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set_theme(style="whitegrid", palette ="pastel");

class LRModel:
  def __init__(self,xdata,ydata):
    self.x = xdata
    self.y = ydata
    self.model = None
  def add_const(self):
    self.x = sm.add_constant(self.x)
  def fit_data(self):
    data_ = sm.OLS(self.y, self.x)
    model_ = data_.fit()
    self.model = model_
    return model_.params

  def plot_data(self):
    plt.figure()
    plt.scatter(self.x.T[1],self.y, c="orange", alpha=0.7)
    plt.plot(self.x.T[1], self.model.predict(), c="red", alpha=0.7)
    plt.savefig('static/data.png')