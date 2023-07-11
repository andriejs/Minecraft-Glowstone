compile:
	rm -rf dist
	pyinstaller Minecraft.spec
	rm -rf build
