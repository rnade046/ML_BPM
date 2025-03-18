### Intro
**Background:** Transcription factors (TFs) play an essential role in regulating gene expression by binding DNA at specific sites. Identifying these TF binding sites has the potential to elucidate mechanisms regulating the cell. [1] Given the size of an organism’s genome, motif discovery in DNA is a complex problem. With the rise of high-throughput technologies, many computational tools have been developed to identify TF binding sites. [2] One such technology, protein binding microarrays (PBMs) allow the identification of specific DNA-protein interaction in vitro. PBMs can be used to develop position weight matrices (PWMs) which characterizes the binding affinity between TFs and DNA sequences. [3] Support vector machines are a type of classifier that has been proposed for biological sequence classification problems. Specifically, the use of PBM data can be used to train an SVM to identify TF binding regions as presented by Hu et al. [4]

**Dataset:** A PBM dataset was obtained from the [DREAM5 TF-DNA Motif Recognition Challenge](https://www.synapse.org/Synapse:syn2887863/wiki/72185). [5]  This data corresponds to all possible 10-mer DNA sequences of 86 mouse TFs. Two types of array systems were implemented, ME and HK. A total of 40526 and 40330 probes were used respectively in each system. The obtained TF consensus sequence obtain from our methods will be compared to known TF binding sites found in the JASPAR database. [6]

**Methods:** Two machine learning methods were implemented to identify potential TF binding sites from the PBM data. In both cases, 80% training/20% testing of the data. Identified TF sequences can be assessed for position statistics to develop a position weight matrix and develop a seq-logo chart. Obtained seq-logo charts will be compared to existing TF binding site consensus sequences. 

(A)	In an attempt to partially recreate the SVM experiment proposed by Hu et al. [4] Our SVM model was developed using the methods outlined in the scikit-learn package in Python. [7]  For training, as selected in the paper, the top 200 probes with that scored the highest binding affinity will be used as positive instances and the last 200 probes will act as negative instances. 

(B)	It was proposed by Zhao et al. that a simpler regression model is sufficient for the identification of TFs. [8] Therefore, our second experiment was conducted using a logistic regression model through the methods found in the scikit-learn package in Python. [7] A feature selection method will be implemented to identify the number of necessary features and optimal features/sequences for developing the model

### References
[1]	J. M. Vaquerizas, S. K. Kummerfeld, S. A. Teichmann, and N. M. Luscombe, “A census of human transcription factors: function, expression and evolution,” Nat. Rev. Genet., vol. 10, no. 4, pp. 252–263, Apr. 2009.

[2]	J. Hu, Y. Zheng, and X. Shang, “MiteFinderII: a novel tool to identify miniature inverted-repeat transposable elements hidden in eukaryotic genomes,” BMC Med. Genomics, vol. 11, no. S5, p. 101, Nov. 2018.

[3]	G. R. G. Lanckriet, T. De Bie, N. Cristianini, M. I. Jordan, and W. S. Noble, “A statistical framework for genomic data fusion,” Bioinformatics, vol. 20, no. 16, pp. 2626–2635, Nov. 2004.

[4]	J. Hu et al., “MD-SVM: a novel SVM-based algorithm for the motif discovery of transcription factor binding sites,” BMC Bioinformatics, vol. 20, no. S7, p. 200, May 2019.

[5]	M. T. Weirauch et al., “Evaluation of methods for modeling transcription factor sequence specificity,” Nat. Biotechnol., vol. 31, no. 2, pp. 126–134, Feb. 2013.

[6]	A. Khan et al., “JASPAR 2018: update of the open-access database of transcription factor binding profiles and its web framework,” Nucleic Acids Res., vol. 46, no. D1, pp. D260–D266, Jan. 2018.

[7]	F. Pedregosa et al., “Scikit-learn: Machine Learning in Python,” J. Mach. Learn. Res., vol. 12, no. Oct, pp. 2825–2830, 2011.

[8]	Y. Zhao and G. D. Stormo, “Quantitative analysis demonstrates most transcription factors require only simple models of specificity.,” Nat. Biotechnol., vol. 29, no. 6, pp. 480–3, Jun. 2011.
