



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

Compute Node: A compute node has to belong to at least one queue to be valid.