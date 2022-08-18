import printing_models_module

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_models_module.print_models(unprinted_designs, completed_models)
printing_models_module.show_completed_models(completed_models)