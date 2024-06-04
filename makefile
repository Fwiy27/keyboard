build:
	python3 -m venv venv
	source venv/bin/activate && \
		pip install -U wheel setuptools && \
		python -m setup bdist_wheel && \
		rm -rf kbd.egg-info && \
		rm -rf build && \
		rm -rf venv