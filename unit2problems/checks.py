import check50

@check50.check()
def indoor():
    """hello world"""
    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)
