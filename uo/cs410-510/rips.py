import gudhi
import matplotlib.pyplot as plt
import numpy as np
# import pprint

off_file = "dtorus.off"

pc = gudhi.read_points_from_off_file(off_file=off_file)
# pc = gudhi.subsampling.choose_n_farthest_points(points=pc, nb_points=500)
print("number of points: " + str(len(pc)))

rips_complex = gudhi.RipsComplex(points=pc)

st = rips_complex.create_simplex_tree(max_dimension=1)
print("number of edges before collapse: " + str(st.num_simplices()))

st.collapse_edges()
print("number of edges after collapse: " + str(st.num_simplices()))

st.expansion(3)
print("number of simplices after expansion: " + str(st.num_simplices()))

pd = st.persistence()
# pd = [x for x in pd if x[0] == 1] # pd in dim 1

ax = gudhi.plot_persistence_diagram(persistence=pd)
ax.set_title(f"Persistence diagram of {off_file}")
plt.show()

ax = gudhi.plot_persistence_barcode(persistence=pd)
ax.set_title(f"Persistence barcode of {off_file}")
plt.show()
