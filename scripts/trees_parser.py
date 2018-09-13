import ast
from helper import get_all_words


AST_OBJECTS = {'func': ast.FunctionDef, 'class': ast.ClassDef}


def list_all_variables_names(trees):
    list_all_names = []
    for tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                list_all_names.append(node.id.lower())
    return get_all_words(list_all_names)


def get_list_objects_name(trees, object_name):
    if str(object_name).lower() == 'var':
        return list_all_variables_names(trees)
    if object_name in AST_OBJECTS.keys():
        list_all_names = []
        for tree in trees:
            for node in ast.walk(tree):
                if isinstance(node, AST_OBJECTS[object_name]):
                    list_all_names.append(node.name.lower())
    return get_all_words(list_all_names)
