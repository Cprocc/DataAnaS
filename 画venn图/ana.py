import xlrd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
data = xlrd.open_workbook("3dataA.xlsx")
table = data.sheet_by_name(u'Sheet1')

a = table.col_values(1)
b = table.col_values(5)
c = table.col_values(9)

venn3(subsets=[set(a), set(b), set(c)], set_labels=('down', 'pl', 'up'),
      set_colors=('r', 'b', 'g'))

plt.show()
