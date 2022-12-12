clean:
	@rm -rf .coverage coverage.xml htmlcov report.xml
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

format:
	@pre-commit run --all-files

test:
	@python -m pytest --cov=simple_file_sorter/ tests/ --durations=0 -vvv
