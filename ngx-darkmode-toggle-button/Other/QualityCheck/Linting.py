import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def linting():
    TasksForCommonProjectStructure().standardized_tasks_linting_for_node_project_in_common_project_structure(str(Path(__file__).absolute()), 1, sys.argv)


if __name__ == "__main__":
    linting()
