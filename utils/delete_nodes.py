from aiida.orm import QueryBuilder, CalcFunctionNode, CalcJobNode, WorkChainNode, WorkflowNode
from aiida.tools import delete_nodes
from aiida import load_profile
load_profile()

qb = QueryBuilder()       # Instantiating instance. One instance -> one query
qb.append([CalcFunctionNode, CalcJobNode, WorkChainNode, WorkflowNode])
nodes = [n[0].pk for n in qb.all()]
pks_to_be_deleted = delete_nodes(
    nodes, dry_run=False, create_forward=True, call_calc_forward=True, call_work_forward=True
)
