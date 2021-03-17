# import numpy and matplot
import numpy as np
import matplotlib.pyplot as plt
#input the number
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
gl_array = np.array(gene_lengths)
ex_array = np.array(exon_counts)
average = sorted(gl_array/ex_array)
print(average)
#set the parameter 
plt.boxplot(average, vert = True, patch_artist = True, meanline = False, showbox =True,showcaps= True, showfliers = True, notch = False)
plt.xticks([],)
#name the fifure
plt.title('the distribution of the average exon length across 10 genes')
#show the result
plt.show()