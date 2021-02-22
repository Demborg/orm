from subprocess import check_output, run
from tempfile import NamedTemporaryFile

def test_print():
    fp = NamedTemporaryFile(mode="w+t")
    fp.write("""
    skriv \"hej världen!\"
    """)
    fp.flush()
    
    result = check_output(["./orm", fp.name]).decode()
    assert result == "hej världen!\n"
