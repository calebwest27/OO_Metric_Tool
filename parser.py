
import ast


def parse_classes(source_code):
    tree = ast.parse(source_code)

    class_nodes = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
    ]

    class_names = {node.name for node in class_nodes}
    classes = []

    for node in class_nodes:
        methods = []
        method_attributes = {}
        response_methods = set()

        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.append(item.name)

                attributes = set()

                for child in ast.walk(item):

                    if (
                        isinstance(child, ast.Attribute)
                        and isinstance(child.value, ast.Name)
                        and child.value.id == "self"
                    ):
                        attributes.add(child.attr)

                    if isinstance(child, ast.Call):
                        if isinstance(child.func, ast.Attribute):
                            response_methods.add(child.func.attr)

                        elif isinstance(child.func, ast.Name):
                            response_methods.add(child.func.id)

                method_attributes[item.name] = attributes

        dependencies = set()

        for child in ast.walk(node):
            if isinstance(child, ast.Name):
                if child.id in class_names and child.id != node.name:
                    dependencies.add(child.id)

        classes.append({
            "name": node.name,
            "methods": methods,
            "method_count": len(methods),
            "method_attributes": method_attributes,
            "dependencies": sorted(dependencies),
            "response_methods": sorted(response_methods)
        })

    return classes
