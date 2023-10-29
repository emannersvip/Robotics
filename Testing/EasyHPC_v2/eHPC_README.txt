
# https://www.w3schools.com/python/python_classes.asp
# https://docs.python.org/3/tutorial/classes.html



# A DC contians clusters
# A cluster includes:
# - Login nodes : *
# - scheduler nodes : *
# - Compute nodes : $
# - App nodes : ^


$: Mandatory in every cluster
*: Mandatory in at least the first cluster. Optional in all others but there has to always
 : be at least one in existence.
^: Optional 

Cluster: A cluster needs at least one login node and scheduler node to be active.
LoginNode: A login node has to belong to at least one cluster.
Compute Node: A compute node has to belong to at least one queue to be valid.

eg.
> ehpc cluster list
> ehpc login list
