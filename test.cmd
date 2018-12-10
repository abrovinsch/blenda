echo Building package...
pip3 install . -q
echo Running:
python3 tests/test_blenda.py
