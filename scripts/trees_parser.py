import ast
from helper import get_all_words_in_listnames, cuts_off_special_names

AST_OBJECTS = {'func': ast.FunctionDef, 'class': ast.ClassDef}


def get_list_all_variables_names(trees):
    list_all_names = []
    for tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                list_all_names.append(node.id.lower())
    list_names = cuts_off_special_names(list_all_names)
    return get_all_words_in_listnames(list_names)


def get_list_objects_name(trees, object_name):
    if str(object_name) == 'variable':
        return get_list_all_variables_names(trees)
    if object_name in AST_OBJECTS.keys():
        list_all_names = []
        for tree in trees:
            for node in ast.walk(tree):
                if isinstance(node, AST_OBJECTS[object_name]):
                    list_all_names.append(node.name.lower())
    list_names = cuts_off_special_names(list_all_names)
    return get_all_words_in_listnames(list_names)
