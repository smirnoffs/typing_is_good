doit:
	# Dependencies should be installed from requirements-dev.txt.
	# Sorts imports in python files.
	isort -rc .
	# Formats python files.
	black .
