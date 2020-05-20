t("space")
    release("space")
    while True:
        image = takeScreenshot()
        data = image.load()
        if isCollide():
            hit("space")
            release("space")